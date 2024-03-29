# IT 领域的 tutorial

From [here](https://yinwang1.substack.com/p/it-tutorial).

最近自己琢磨了一下一些实用的技术，比如某些 Web 前端技术，Kubernetes 的用法等等。我发现这些技术的官方教程普遍存在严重的问题，让人很不容易看下去。有些被叫做 tutorial，可是却仍然很难看懂。想了一下，计算机技术的教育一直以来都是这样，造成了很高的门槛。

初步总结一下，我觉得这些入门教程存在以下几个问题：

Web 前端 tutorial，普遍的问题是喜欢让学生做一些“现实应用”，比如小游戏。本来这技术用非常小的，几行代码的例子就能说明白，非得设计一个类似 tic-tac-toe 那样的游戏。

tic-tac-toe 是一个简单的游戏，然而它的实现对于介绍一个 web 前端框架，仍然过于复杂。写了好几节课还没有明白最后做出什么。学到一半的时候，就已经开始迷糊这个技术的要点在哪里了。我到底是在学这个技术比起其它技术先进的地方，还是在折腾那个游戏到底该怎么写？

你会想玩 tic-tac-toe 这样的游戏吗？我觉得大部分人都会觉得这游戏非常无聊。自己不想玩的游戏，却要去实现它，这是不是太辛苦了？所以这类 tutorial 的设计初衷是“有趣”，而其实非常的无聊，毫无动力可言。

像 Kubernetes 的教程，就更糟糕。他们设计了一个叫做「minikube」的东西，让初学者可以在本地架起一个cluster，然后用教程的一些「minikube xx」命令来操作这个 cluster。然而这个 cluster 一起来，什么事都还没让它做呢，就消耗大量的 CPU，高达 60%，风扇狂转，机身滚烫。

查了一下网络，发现这个问题很常见，已经在 GitHub 上面讨论了几年之久：https ://github.com/kubernetes/minikube/issues/3207。这个讨论从 2018 年 10 月，一直到 2021 年 3 月，后来不了了之被 close 了，直到今天还是没有结果。我现在仍然遇到这个问题，另一个同事按照这个说明进行，也遇到同样的问题。

minikube 只是一个学习用的 cluster，却设计了自己的命令行。这些命令行跟正式的 Kubernetes 命令 kubectl 的用法又不一样。作为一个学习工具，有什么必要设计自己的命令行呢？人们只是拿它学习，用了它的命令行，到时候却不能用到实际的应用中。与其花功夫去设计 minikube 玩具，还不如直接告诉人们怎么从头开始，用实用的软件搭起一个“工业级”的 cluster。

消耗大量 CPU 时间这个事情，几年时间居然得不到解决，这会让人怀疑 Kubernetes 这整个技术的资源管理是不是有问题，在实际的应用中会不会出问题。而且这显示 Kubernetes 的人员组织也有问题，似乎很混乱。感觉很多人在各搞各的，最后拼不到一起，连官方 tutorial 都是好几套写法。这一节说你先做 A，下一节又说你先做 B，可是 A 和 B 之间却没有关系，根本就是不同的人写的。

minikube 的文档还有一个问题，经常把之前从来没讲过的概念一下子摆出来，说我们这一节要介绍 blah blah blah…… 一般人看到这些就头晕了。我觉得一个好的教学文档，不应该把还没定义的术语列举出来，就算作为一个引文也不应该，因为这会让人迷惑和害怕。

这些文档还有很多很多其他问题，比如前后不一致，跟实际的设计不同步，等等。你以为这么多大公司在推广Kubernetes，它的文档应该是跟当前实现同步的？然而却不是。看到中间就会发现某些命令行，按照文档上输入，就是不管用。得到其他地方搜索这问题，也许才会明白是怎么回事，但也许发现所有人都是糊涂的。

还有些时候，文档作者为了“方便”，使用类似这样的命令行：

export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"

这样拷贝粘贴确实方便了，直接把命令的输出放进一个变量里，然而用户是不可能记住这样的命令的，他们会疑惑这命令怎么这么奇怪，难道 Kubernetes 实际得这样用？然而却不是的，这些值都是可以从简单的命令输出里拷贝粘贴的，而不需要输入这么复杂的命令行。本来简单示例解释一下就行了，却弄得如此复杂和“自动化”。

作为一个大量普及的技术的入门文档，这些是不应该出现的问题，造成了不必要的脑力开销和困惑。
