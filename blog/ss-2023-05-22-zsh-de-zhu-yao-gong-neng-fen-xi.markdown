# zsh 的主要功能分析

From [here](https://yinwang1.substack.com/p/zsh).

换掉 zsh 回到 bash 之前，为了确保我没有漏掉什么好东西，我又搜索了一下“zsh better than bash”。发现除了“命令行补全”，更换“主题”之类 bash 本来就可以有的功能，zsh 恐怕就只剩下“直接输入目录名就能 cd”这样的了。也就是说你不用打 cd /etc，而是直接打 /etc，就能到 /etc 目录。

<span>谁在乎多打少打 cd 两个字？这也叫超越 bash 的优势？然而这个功能被很多推 zsh 的文章（比如</span>[https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/](https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/)<span>）排在 zsh 的“太多 feature”的首位。可笑不？</span>

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f4fa957-9f94-4083-9673-b6042d92d68c_640x301.jpeg)

如果 Automatic cd 能被列在“主要 feature”的首位，这说明 zsh 还能有什么重要的 feature？我发现这段话堪称经典，值得仔细分析回味一下。几年前我是怎么落入这个傻的不行的圈套的？😄

很多人可能没有发现，Automatic cd 不但没有节省什么时间，而且并不是什么好东西。cd xyz 明确的说明了用户的意图是“切换目录到 xyz”。如果没有了 cd，直接输入 xyz，就和“执行 xyz 这个命令”的语义混淆了。如果能出现这样的混淆，就需要用户输入的时候更加小心，不然本来想输入命令，却被误以为要切换目录。混淆之后，再花时间来分析和改正，需要浪费用户更多的时间和脑力。而且这种事情会反复发生，为此浪费的时间，因此产生的烦躁累积起来，就很多了。这种混淆是完全没必要的，如果输入 cd 就不会发生这种混淆。所以明确输入 cd 两个字是更好的做法，简单明了，没有歧义。

再看看第二个主要 feature（Recursive path expansion）：说 zsh 能自动把 “/u/lo/b” 这样的输入扩展成“/usr/local/bin”？谁用过这功能？反正我不知道它有这功能，知道了我也不会用它。这样的自动扩展让人以为“方便”，而其实很容易混淆，浪费更多时间。要是 /u/lo/b 对应着多个可能的扩展怎么办？而且这种歧义是指数增长的。如果每级目录的名字有 2 种可能性，3 级目录就有 8 种可能性。出现了歧义，用户就得去选择，选择就需要花时间和脑力。而且要是前面或者中间的目录前缀你打错了字，就会发现怎么展不开，或者展开是错的，然后又要回去改，经历更多麻烦。所以这些目录名，我宁愿一个个的按 tab 展开，确认前一个扩展对了，再开始输入下一个，而不是一次性输入/u/lo/b 这样的，然后按 tab 一下子展开。

第三个 feature 就更容易造成混淆：Spelling correction and approximate completion。按 tab 之后，它会试图把你打错的文件名或命令自动更正。但我第一次察觉到这个功能，就发现非常容易出错。我刚打了两个字，本来想 tab 补全一个命令，结果因为其中一个字打错了，所以它给我补全成了完全不同的另一个命令。我很惊讶，我没想到命令行怎么会变成那个样子，我从来没听说过那个命令。仔细看了一会才发现，原来是因为这两个字母出现在另一个命令名字的中间，所以 zsh 就给我“自动纠错”了。我宁愿它当时就什么都不要做，什么都别自动更正，这样我立即就会发现其中一个字母打错了，马上改掉，而不是看到自动更正的命令，然后才去想我刚才做了什么，展开成这样奇怪的结果，我在做什么……？

第四个 feature（Plugin and theme support）就不多说了。不但是多余的，而且这些花哨的配置 bash 也可以有。

另外，这段话开头说“some just minor improvements to Bash”，既然以上的鸡毛蒜皮事情能算 “major improvement”，那什么才算是“minor improvements”呢？我感觉就是那些微妙的 shell 语言改动了。然而恰恰是那些minor 的语言改动，让你无法表达想要的东西，让网上搜到的 bash 的现成答案都不能拿来用。就这样，完美地制造了一些无解的问题。

很多人换成 zsh，可能都是因为看了这样的文章，列出了这“多种 feature”，而没有思考过，这些 feature 真的重要，真的有用吗？自己其实没发现有什么好，就开始给别人推荐，结果大家都被这种洗脑宣传传染了。zsh 如此莫名其妙的大规模传播，人人都说它更好，却不知道好在哪里了，甚至成为了 macOS 的 default shell，我简直觉得这是 Matrix 在搞鬼了。😄
