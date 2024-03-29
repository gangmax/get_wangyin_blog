# 计算机视觉的隐藏技巧

From [here](https://yinwang1.substack.com/p/b75).

AI 领域还有一个隐藏很深的技巧，用于让人们相信计算机视觉超越了人类。那就是他们的图片库（比如ImageNet）里面有很多刁钻而不常见的事物，或者把某些事物的品种分得很细，要你说出它具体的名字来。比如某种海洋里的奇怪动物，某种不常见的植物，或者让你说出一只狗，一朵花甚至一头鲸的具体品种来。

以大量这种图片来刁难人类测试者，这样神经网络就显得更厉害一些。然后他们就可以说，你看人类做 top-5 就已经很难了，这么多的东西都没见过，说不出名字来，这就是为什么我们使用 top-5 作为标准。但是人们没想到的是，这图片库的选材根本就是故意刁难人的，能否说出那些稀奇事物的名字，这个根本就不重要。

如果有太多品种的事物，计算机确实可能更容易知道它叫什么名字。这就像搜索引擎，没人能超越搜索引擎检索信息的能力。然而对于人们常见的事物，计算机却无法每次都准确地识别出它们，top-1 识别率很低，这是会要命的事情。而且就算识别出来，计算机也只是知道它们名字，却不知道它们的性质，不知道它们的组成部分和材质是什么。

再说了，说出一只狗的具体品种，这种事真的能衡量视觉能力吗？这只是在玩文字游戏。很少有人见过所有品种的狗，但是他们看到一只未知品种的狗，却都能比较准确地知道那是狗。计算机就没有这种能力，要是有一只很特别，图片库里从来没出现过的狗，它是很难知道那是一只狗的。人还能识别抽象的艺术作品或者装饰品里面是狗，三岁小孩都能知道。然而这对于计算机来说却几乎是不可能的。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcc459db-df4b-4b86-94eb-c799de731143_550x412.jpeg "IMG_8933.jpeg")

