## 讨厌的 C# IDisposable 接口

我们 team 快被 C# 里面的各种 [IDisposable](https://msdn.microsoft.com/en-us/library/system.idisposable(v=vs.110).aspx) 对象给折腾疯了！[Roslyn 静态分析](https://github.com/dotnet/roslyn-analyzers)一打开，给出几百个警告，说你没有调用有些对象里的 Dispose 方法。奇葩的是，有些很小的对象，包括 [ManualResetEvent](https://msdn.microsoft.com/en-us/library/system.threading.manualresetevent(v=vs.110).aspx), [Semaphore](https://msdn.microsoft.com/en-us/library/system.threading.semaphore(v=vs.110).aspx), [ReaderWriterLockSlim](https://msdn.microsoft.com/en-us/library/system.threading.readerwriterlockslim(v=vs.110).aspx) 都是 IDisposable。按官方的“规矩”，你得显式的调用 Dispose 方法进行“释放”，而不能依赖 GC 进行回收。

问题是，很多时候你根本搞不清楚什么时候该释放一个对象，因为它存在于一个复杂的数据结构里面，到处被引用，所以你很难搞清楚什么时候不会有代码再用它。如果你过早调用 Dispose 方法，释放了对象里的资源，但其实还有人在用它，就会出现严重的错误。这问题就像 C 语言里面的 free，你很多时候不知道该不该 free 一块内存。如果你过早的 free 了内存，就会出现非常严重的内存错误。所以对于复杂的数据结构，比如图节点，你就只好痛苦的给对象手动加上引用计数。或者如果内存够用，你也不需要分配释放很多中间结果的话，你就干脆到算法结束以后再一并释放它们……

是的 C# 有垃圾回收（GC），所以你以为不用再考虑这些低级问题了。不幸的是，IDisposable 接口把这噩梦给带回来了。以前在 Java 里面用此类对象，从来没遇到过这么麻烦的事情，最多就是打开文件的时候需要记得最后关掉。所以我很怀疑 C# 里的那些像 Semaphore 之类的小东西是否真的需要显式的“释放资源”。

不得已之下，我用 JetBrains 出品的反汇编器 [dotPeek](https://www.jetbrains.com/decompiler) （好东西呀！）反编译了 .NET 的库代码。结果发现好些库代码其实完全没必要实现 IDisposable 接口。这说明有些 .NET 库代码的作者其实都没有弄明白什么时候该实现 IDisposable 接口，以及如何有意义地实现它。这些类包括常用的 HashAlgorithm 甚至 MemoryStream。其中 HashAlgorithm（各种 SHA 算法的父类）的 Dispose 方法是完全没必要的，它看起来是这个样子：

    protected virtual void Dispose(bool disposing)
    {
        if (disposing)
        {
            if (HashValue != null)
                Array.Clear(HashValue, 0, HashValue.Length);
            HashValue = null;
            m_bDisposed = true;
        }
    }

看明白了吗？它不过是在把内部数组 `HashValue` 的每个元素清零，然后把指针设为 null。之后我要讲一下，在 Dispose 方法里把成员设为 null，其实并不会导致更快的内存释放，所以对资源释放一点用都没有。有人可能以为这是为了“安全”考虑，然而 IDisposable 是用于释放“资源”的接口，把安全清零这种事情放在这个接口里面，反而会让人造成疏忽。而且从源代码里的注释看来，HashAlgorithm 的这个方法就为了释放资源，而不是为了什么安全的考虑。这些库代码实现 IDisposable，意味着这个接口会通过这些库代码不必要的传递到用户代码里面去，导致很多不知情用户的代码被迫实现 IDisposable，造成“传染”。

另外，我发现 AutoResetEvent，ManualResetEvent，ReaderWriterLockSlim，Semaphore 这些 IDisposable 对象，里面的所谓“资源”都是很小的 event 对象，而且它们都是被 SafeHandle 指向的。SafeHandle 本身有一个“析构函数”（finalizer），它会在被 GC 回收的时候，自动调用 Dispose 方法。也就是说，你其实并不需要手动调用这些对象的 Dispose 方法。这些对象占用资源很少，GC 完全应该有能力释放它们占用的系统资源（Win32 Event 对象）。

什么时候该实现 IDisposable 接口，我建议使用 .NET 的开发人员（包括微软自己的员工）先看看[这篇 blog](http://blog.stephencleary.com/2009/08/first-rule-of-implementing-idisposable.html)（看完之后我还有其它的推荐）。简言之，如果你的对象的 Dispose 方法只是在把一些成员对象设为 null，那么你根本就不需要实现 IDisposable。为什么呢？因为把对象引用设为 null 并不等于 C 语言里面的 free，它并不能让 GC 更快的回收那份内存，就算你的对象里面有一个很大的 byte[] 数组也一样。

其实在 C# 里面，你没有任何办法可以手动回收内存，你一定要依赖于 GC。就算你实现 Dispose，在里面把成员设置为 null，内存也只有等下次 GC 执行的时候才能被回收。所以你还不如就把外层对象的引用设为 null（如果是局部变量就让它自然离开作用域），GC 下次执行的时候，就会自动把里面的对象也给回收了。完全不需要你实现 Dispose 方法，你实现了也不能更加及时的回收内存。为什么 GC 会回收里面的对象呢？去看看 GC 的工作原理就知道了！简言之，Dispose 不是用来给你回收内存用的。

微软其它 team 的童鞋们，欢迎来人来函跟我讨论你们对待 IDisposable 的做法。我现在已经有一套用于对付 IDisposable 的策略，准备整理之后在 team 内部推行。我还准备写一个“终极指南”，用于简化对 IDisposable 的处理，你们的经验和讨论将对此很有帮助。
