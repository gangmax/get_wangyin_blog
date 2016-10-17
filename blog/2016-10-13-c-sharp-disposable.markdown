## 讨厌的 C# IDisposable 接口

我们 team 快被 C# 里面的各种 [IDisposable](https://msdn.microsoft.com/en-us/library/system.idisposable(v=vs.110).aspx) 对象给折腾疯了！先来科普一下，如果你没有用过 C# 和 Windows 编程，IDisposable 是 C# 针对“资源管理”设计的一个接口，它类似于 Java 的 [Closeable](https://docs.oracle.com/javase/7/docs/api/java/io/Closeable.html) 接口。这类资源管理接口一般提供一个“方法”（比如叫 Dispose 或者 Close），你的资源（比如文件流）实现这个方法。使用这个资源的人在用完之后调用这个方法，表示“关闭资源”。比如，文件打开用了之后，我们一般都会调用 close 进行关闭，就是这个原理。

C# 和 Java 非常类似，可是 C# 的 IDisposable 接口引起的头痛，却比 Java 的 Closeable 大很多。经过我分析，这一方面是因为 .NET 的库代码里面实现了很多没必要的 IDisposable，以至于很容易的传染到很多用户代码里面去。另一方面，是由于微软的编码规范和 Roslyn 静态分析引起的误导作用，引起用户对于 IDisposable 接口的要求（比如调用 Dispose 方法）过度在乎。

回来说说我们的代码，本来代码没那么多问题的，结果把 [Roslyn 静态分析](https://github.com/dotnet/roslyn-analyzers)一打开，立马给出几百个警告，说你“[没有调用 IDisposable 对象里的 Dispose 方法](https://msdn.microsoft.com/en-us/library/ms182328.aspx) ”。奇葩的是，有些很小的对象，包括 [ManualResetEvent](https://msdn.microsoft.com/en-us/library/system.threading.manualresetevent(v=vs.110).aspx), [Semaphore](https://msdn.microsoft.com/en-us/library/system.threading.semaphore(v=vs.110).aspx), [ReaderWriterLockSlim](https://msdn.microsoft.com/en-us/library/system.threading.readerwriterlockslim(v=vs.110).aspx) 都是 IDisposable。按官方的“规矩”，你得显式的调用它们的 Dispose 方法进行“释放”，而不能依赖 GC 进行回收。所以你的代码经常看起来就像这个样子：

    void foo()
    {
      var event = new ManualResetEvent(false);
      // 使用 _event ...
      event.Dispose();
    }

貌似没什么困难嘛，我们把每个对象的 Dispose 方法都调用一下，不就得了？然而问题远远不是这么简单。很多时候你根本搞不清楚什么时候该释放一个对象，因为它存在于一个复杂的数据结构里面，同时被很多代码引用，所以你很难搞清楚什么时候不再有人用它。如果你过早的调用了 Dispose 方法，释放了对象里的资源，而其实还有人在用它，就会出现严重的错误。这问题就像 C 语言里面的 free，很多时候你不知道该不该 free 一块内存。如果你过早的 free 了内存，就会出现非常严重而蹊跷的内存错误，比泄漏内存还要严重很多。举一个例子：

    void main()
    {
        int *a = malloc(sizeof(int));
        *a = 1;

        int *b = malloc(sizeof(int));
        *b = 2;

        free(a);

        int *c = malloc(sizeof(int));
        *c = 3;

        printf("%d, %d, %d\n", *a, *b, *c);    
    }

你知道这个 C 程序最后是什么结果吗？所以对于复杂的数据结构，比如图节点，你就只好痛苦的给对象手动加上引用计数。或者如果内存够用，你也不需要分配释放很多中间结果，那你就干脆到算法结束以后再一并释放它们……

是的 C# 有垃圾回收（GC），所以你以为不用再考虑这些低级问题了。不幸的是，IDisposable 接口以及对于它“兢兢业业”的态度，把这噩梦给带回来了。以前在 Java 里用此类对象，从来没遇到过这么麻烦的事情，最多就是打开文件的时候要记得关掉。我从来不记得 Java 的等价物（[Closeable](https://docs.oracle.com/javase/7/docs/api/java/io/Closeable.html) 接口）引起过这么多的麻烦，Java 的 [Semaphore](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/Semaphore.html) 根本就没有实现 Closeable 接口，不需要调用什么 Close 或者 Dispose 之类的。作为一个眼睛雪亮的旁观者，我开始怀疑 C# 里的那些像 Semaphore 之类的小东西是否真的需要显式的“释放资源”。

为了摸清实情，我用 JetBrains 出品的反编译器 [dotPeek](https://www.jetbrains.com/decompiler) （好东西呀）反编译了 .NET 的库代码。结果发现好些库代码实现了完全没必要的 IDisposable 接口。这说明有些 .NET 库代码的作者其实没有弄明白什么时候该实现 IDisposable ，以及如何有意义地实现它。这些有问题的类，包括常用的 HashAlgorithm（各种 SHA 算法的父类）和 MemoryStream。其中 HashAlgorithm 的 Dispose 方法完全没必要，这个类的源代码看起来是这个样子：

    public abstract class HashAlgorithm : IDisposable, ICryptoTransform {
      ...
      protected internal byte[] HashValue;
      ...
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
    }

看明白了吗？它不过是在把内部数组 HashValue 的每个元素清零，然后把指针设为 null。这个库代码作者没有搞明白的是，如果你的 Dispose 方法只是在把一些成员设为 null，那么你根本就不需要实现 IDisposable。为什么呢？因为把引用设为 null 并不等于 C 语言里面的 free，它并不能立即回收那份内存，就算你的对象里面有一个很大的数组也一样。我发现有些 C# 程序员喜欢在使用对象之后把引用赋值为 null，就像这样写代码：

    void foo()
    {
      BigObject x = new BigObject();
      // ...
      // 使用 x 指向的对象 ...
      // ...
      x = null;
    }

`x = null` 是毫无意义的。写出这样的代码，说明他们不明白 GC 是如何工作的，以为把引用设为 null 就可以释放内存，以为不把引用设为 null，内存就不会被回收！再进一步，如果你仔细看 HashAlgorithm 的源代码，就会发现 HashValue 这个成员数组其实完全没有必要存在，因为它保存的只是上一次调用 ComputeHash() 的结果而已。这种保存结果的事情，本来应该交给使用者去做，而不是包揽到自己身上。这个数组的存在，还导致你没法重用同一个 HashAlgorithm 对象，因为有共享的成员 HashValue，所以不再是 thread safe 的。有点跑题了……

其实在 C# 里面，你没有办法可以手动回收内存，因为内存是由 GC 统一管理的。就算你实现 Dispose，在里面把成员设置为 null，内存也只有等下次 GC 执行的时候才可能被回收。举一个例子：

    class Foo : IDisposable
    {
      private byte[] _data = new byte[1000000000];

      public void Dispose()
      {
        _data = null;    // 没用的
      }
    }

在这个例子里面，Foo 类型的 Dispose 只是在把 _data 设为 null，这是毫无意义的。如果你想释放掉这块数组，那么你只需要等不再有人使用 Foo 对象。比如：

    void UseFoo()
    {
      Foo foo = new Foo();
      // 使用 f...
      foo.Dispose();  // 没必要
      foo = null;     // 没必要
    }

这里的 `foo.Dispose()` 是完全没必要的。你甚至没必要写 `foo = null`，因为 foo 是一个局部变量，它一般很快就会离开作用域的。当函数执行完毕，或者编译器推断 foo 不会再次被使用的时候，GC 会回收整个 Foo 对象，包括里面的巨大数组。

所以正确的做法应该是完全不要 Dispose，不实现 IDisposable 接口。有些人问，要是 Foo 对象被放进一个全局哈希表之类的数据结构，GC 没法释放它，就需要 Dispose 了吧？这也是一种常见的误解。如果你真要回收全局哈希表里的 Foo 对象，你只需要把 Foo 对象从哈希表里面删掉就可以了。一旦哈希表对 Foo 对象的引用没有了，GC 运行的时候就会发现它成了垃圾，里面的 _data 数组自然也是垃圾，所以一起就回收掉了。

所以简言之，Dispose 不是用来给你回收内存用的！在 Dispose 方法里把成员设为 null，并不会导致更快的内存释放，所以对资源释放一点用都没有。有人可能以为 HashAlgorithm 是为了“安全”考虑，所以在 Dispose 方法里对数组清零。然而 IDisposable 是用于释放“资源”的接口，把安全清零这种事情放在这个接口里面，反而会让人误解，造成疏忽。而且从源代码里的注释看来，HashAlgorithm 的这个方法确实是为了释放资源，而不是为了什么安全考虑。这些库代码实现 IDisposable，意味着这个接口会通过这些库代码不必要的传递到用户代码里面去，导致很多不知情用户的代码被迫实现 IDisposable，造成“传染”。

另外，我发现 AutoResetEvent，ManualResetEvent，ReaderWriterLockSlim，Semaphore 这些 IDisposable 对象，里面的所谓“资源”，归根结底都是一些很小的 event 对象，而且它们都继承了 SafeHandle（比如 SafeWaitHandle）。SafeHandle 本身有一个“析构函数”（finalizer），它看起来是这个样子：

    ~SafeHandle()
    {
        Dispose(false);
    }

当 SafeHandle 被 GC 回收的时候，GC 会自动自动调用这个析构函数，进而调用 Dispose。也就是说，你其实并不需要手动调用这些对象（例如 ManualResetEvent, Semaphore 之类）的 Dispose 方法。这些对象占用资源很少，GC 完全应该有能力释放它们占用的系统资源（只不过包含一些 Windows API 里的 event 对象）。

微软官方文档和 Roslyn 静态分析说一定要调用 Dispose，其实是杞人忧天，把不是问题的问题拿出来让人心惊胆战，结果把自己的代码给搞复杂了。很多人把 Roslyn 静态分析的结果很当回事，而其实看了源代码之后，我发现 Roslyn 关于 Dispose 的静态分析实现，是比较初级的作法（连流分析都没实现），所以结果是非常不准确的。而且它们给出的警告信息有严重的误导性质，比如[CA1001](https://msdn.microsoft.com/en-us/library/ms182172.aspx)警告对你说：“Types that own disposable fields should be disposable。” 如果你严格遵循这一“条款”，让所有含有 IDispoable 的成员的类都去实现 IDisposable，那么 IDisposable 接口就会从一些很小的对象（比如 Semaphore），很快扩散到几乎所有的对象里去。每个对象都实现 IDisposable 接口，却没有任何对象真正的在释放资源。最终结果是，你会在程序结束的时候才能释放这些资源。很有意思，你的一片好心和勤奋努力，导致的是比什么都不做更坏的结果 ;)

什么时候该实现 IDisposable 接口，我建议使用 .NET 的开发人员都先看看[这篇 blog](http://blog.stephencleary.com/2009/08/first-rule-of-implementing-idisposable.html)，看完之后我还有其它的推荐。微软其它 team 的童鞋们，欢迎来人来函跟我讨论你们对待 IDisposable 的做法。我现在已经有一套用于对付 IDisposable 的策略，正在逐渐的潜移默化给同事们。我还准备写一个“指南”，用于简化对 IDisposable 的处理。
