# 系统配置：YAML vs GUI

From [here](https://yinwang1.substack.com/p/yaml-vs-gui).

又看了一点 Kubernetes 的配置方法，发现它的问题已经比较明显了。很多人都说 Kubernetes 配置很繁琐，而且很多人以为这种系统就是这么繁琐，但我觉得这是因为设计思路的错误导致的。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7da238b4-dbd5-4057-a8f7-44bdffa9bb98_640x372.jpeg)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2c19470-3fb7-4d27-b329-cb15bf23224a_640x559.jpeg)

为了理解这个问题，可以比较如下这两幅图。图 1 是 Kubernetes 文档里的一段配置，图 2 是 macOS 的配置中心。它们都是在「配置」系统，可以表达的内容都差不多。然而很显然，macOS 的配置中心比较直观，而 Kubernetes 的配置方式繁琐而容易出错。为什么会这样呢？难道 macOS 这样的 GUI 配置有什么不可取代的地方？我觉得是的。

macOS 配置中心的这个 GUI，其实表达的就是类似于 YAML 那样的“树状”嵌套结构。然而使用 GUI 的时候，用户每次只会看到这棵树的一级，或者比较小的一部分。用户可以根据需要，一层层的点开，用直观的下拉菜单，滚动条，按钮，文本框等方式输入需要的参数。这种 GUI 和 YAML 的不同点在于，用户的操作受到 GUI 的导航和限制，所以无法把内容填进错误的位置，也无法把配置的名称写错。用户可以从界面上直接看到有哪些地方可以改，参数应该是什么样的形式，而不需要去查文档。

图 3 是我最近常用的 Vivaldi 浏览器的配置页面，也差不多。左边分了大类之后，右边是 GUI 的组件。配置什么属性，它有哪些选项，那些是合法的值，都一目了然，不会弄错。那个调整上下文菜单的地方，还可以使用拖拽的方式来选择自己常用的功能，拖动调整顺序，都比较方便。这样的方式，你不可能把本来没有的功能写进上下文菜单里。要是这个用 YAML 来配置，就会很麻烦了。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b3ada1c-ac37-4c32-86c2-6feb0401274c_640x522.jpeg)

Kubernetes 的 YAML 设计，相当于把这些 GUI 配置的内容都用 YAML 的形式实现，全都堆在一起，很不容易找到需要的信息，不知道它们表达的是什么意思。这种 YAML 配置甚至可以有几层的“继承”关系，跟面向对象语言的 class 继承一样，每一层都可以设置同样的 key，各种 override，所以到后来你可能都不知道到底那个地方设置的 value 在起作用了。

用户很难记得这 YAML 应该是什么样的格式，哪个 key 应该在哪个 key 的下一级，哪些应该在同一级，每个地方可以有哪些选择，那些配置的 key 应该叫什么名字，很容易拼错。如果有一点差错，Kubernetes 就找不到需要的内容，配置就不能起作用。而且 Kubernetes 对此经常没有提示和报错，只是静悄悄地把配置里写错的地方忽略了，结果你就不知道到底是哪里写错了，所以不起作用。只好用反复试错的方式来进行，就非常繁琐了。

我已经在 Kubernetes 这些 YAML 配置里看到了等价于“变量定义”，“文件系统目录”等概念，只不过用更糟糕而不方便的形式实现了出来。如果你继续往下看文档，会发现 Kubernetes 居然可以在配置文件里调度并发计算，所以俨然这个YAML 配置会发展成为一个“编程语言”。这正好对应了 Guy Steele 之前总结出的规律——任何配置文件发展到一定阶段，都会变成一种糟糕的编程语言。Kubernetes 这种基于 YAML 的配置，可能会变成最糟糕的编程语言，比 shell 脚本还要糟糕。

所以 Kubernetes 所谓的「Infrastructure as YAML」这个理念，我觉得是相当糊涂扯淡的。YAML 比 JSON 只是语法简单了一些，但它们的问题是一样的，因为没人能记得里面应该是怎么样的结构。同样的原因，基于 JSON 文件配置的一些软件也很难配置，比如 Visual Studio Code。很简单的一些配置，你都得到网上搜索现成的 JSON 配置，拷贝到vscode 的配置文件里，而且还要担心放错了地方不起作用。

这些软件的配置方式可以说是非常糟糕的设计，比 Unix 和 Emacs 等传统的配置文件还要糟糕。
