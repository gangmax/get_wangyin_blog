## 一道 Java 面试题

关于程序员对 Java 类型系统的理解，比较高级的一个面试问题是这样：

<div class="language-java highlighter-rouge">

<div class="highlight">

    public static void f() {
        String[] a = new String[2];
        Object[] b = a;
        a[0] = "hi";
        b[1] = Integer.valueOf(42);
    }

</div>

</div>

这段代码里面到底哪一行错了？为什么？如果某个 Java 版本能顺利运行这段代码，那么如何让这个错误暴露得更致命一些？

注意这里所谓的「错了」是本质上，原理上的，而不一定是 Java 编译器，IDE 或者运行时报给你的。也就是说，你用的 Java 实现，IDE 都可能是错的，没找对真正错误的地方，或者没告诉你真正的原因。

如果你知道哪里错了，并且知道「为什么」错了，可以联系我。
