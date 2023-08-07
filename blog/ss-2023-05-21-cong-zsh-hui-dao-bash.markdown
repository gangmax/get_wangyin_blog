# 从 zsh 回到 bash

From [here](https://yinwang1.substack.com/p/zsh-bash).

不知不觉用了几年的 zsh，起初是因为别人都说 zsh 更好，就试了一下。没想到后来 macOS 升级，把系统默认的shell 换成了 zsh，就以为 zsh 真的很好。但这几天写一些方便工作用的 shell 脚本（其实也就是几行的那种函数），发现 zsh 的语言并不比 bash 的好，有些地方也许更差一些。

shell 语言本来就是垃圾，但是 zsh 却又跟 bash 的语言有少数不同。如果要用 zsh 写脚本，就得再理解一些变种垃圾语法。好不容易在网上找到如何用 bash 的离奇语法表达某个本来很简单的事情，结果用 zsh 就不灵，得换一种稍有不同的离奇语法才行。虽说最终的结果只是稍有不同，但要找到答案其实很费时间，因为失之毫厘谬以千里。

有些其它语言里很简单的事情，比如如何把从某命令行输出拿到的字符串分切成一个数组（split），我至今没有搞明白zsh 要怎么写，网上搜出来的“bash 答案”全都不灵。如何表达一个数组的长度？bash 必须用很奇葩的语法，而 zsh 又不一样。等你好不容易搞明白，如果遇到某个 server 没有 zsh，只有 bash，又不让你自己装东西那种，那就得再改回去。

于是我忽然想起这件事来：zsh 到底有什么好？回想了一下，zsh 也就是提供了一些五颜六色花哨的 theme 而已。一旦装上 oh my zsh 那东西，整个 .zshrc 文件就给变了样，多了一大堆东西，太多的注释。命令行补全，shell history，都变成了某些其他人认为“方便”的形式，而其实很混乱。

每个 theme 都有太多花哨，好不容易找到个简单点的 theme（af-magic），可是每次拷贝 terminal 的内容做笔记，都得把背景上那个 user@host 的水印给一起 copy 下来。另外一些 theme，总喜欢放一些奇怪的花样字符在提示符里，拷贝粘贴到其他地方就成了乱码。这叫做方便？感觉 zsh 是拿来看的，不是拿来用的。

之前我还试过一种新鲜的 shell 叫 fish，开头也是看起来很“先进”和“高效率”的样子，等你需要写点自动化的脚本才发现它的语言有多垃圾，比 bash 还要差很多。zsh 的语言没有 fish 那么差，基本和 bash 差不多，但总有那么一点点差别，让你又浪费很多时间在上面。总之，不能指望任何 unix shell 的语言是好语言。

后来忽然有一天，我问自己，我为什么要用 fish？于是忽然就换回了 bash。结果过了一段时间，有人给我推荐 zsh，我觉得这个语言应该和 bash 一样的，可能会好一点，于是又上了贼船…… 如果你知道一些 Unix 的历史，就知道以前还出现过一些新鲜的 shell，什么 csh，ksh，tcsh，…… 现在都成了昨日黄花 😄

总是有人前仆后继，要设计新的 shell，却又不明白好的 shell 语言应该是什么样的。每一次觉得新鲜的尝试，最后都是一样的结局。所以我现在又再次轮回，想换回 bash，结果发现 macOS 自带的 bash，启动居然会提示你 default shell 已经是 zsh 了，还提示你如何切换到 zsh（如图）。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1fe050b-afd0-40c6-90a2-257dee1e005c_640x429.jpeg)

我可不想每次打开 terminal 都看到这样的提示。找了一会想把它去掉，却没找到这提示是在什么启动脚本里。结果搜索了一下网络，发现必须要在 .bash_profile 里加上这样一行，才能去掉这个提示：

  export BASH_SILENCE_DEPRECATION_WARNING=1

你可以用 grep 或 strings 在 macOS 自带的 /bin/bash 二进制文件里找到这个字符串：please run `chsh -s /bin/zsh`。

~ $ grep 'please run `chsh -s /bin/zsh`' /bin/bash

Binary file /bin/bash matches

~ $ strings /bin/bash | grep zsh

/bin/zsh

The default interactive shell is now zsh.

To update your account to use zsh, please run `chsh -s /bin/zsh`.

所以这提示不是在某个启动脚本里，而是改在了 macOS 自带的 bash 的代码里。改了 bash 的二进制代码来强推zsh，这个做法也太离谱，让人感觉很不正常。一般人最多也就在默认启动脚本（比如 /etc/profile）里暂时放个提示，用户可以随时删掉，不至于连二进制代码都改了，就为了提示大家用 zsh。

修改 bash 的 C 语言代码，然后编译 bash，这比起修改 /etc/profile 配置文件，实在是太费工夫。为什么有人要做这样的事情呢？除非他们非常不想让人用 bash。但是 zsh 并没有比 bash 好，为什么这么想让大家都用 zsh 而不用 bash 呢？这就是疑点了。

网络上能找到的其它去掉这个提示的办法，就只有 brew install bash，而不用系统自带的 bash。如果你不幸升级到了最新的 macOS，那对不起，brew 告诉你这个 os 版本太新，还没有 bash。如果要把系统默认 shell 改成brew 的bash，用 chsh -s /usr/local/bin/bash 居然还不行，说这个是 non-standard shell，得想其它办法。

~ » chsh -s /usr/local/bin/bash                 1 ↵ yinwang@tofu

Changing shell for yinwang.

Password for yinwang:

chsh: /usr/local/bin/bash: non-standard shell

（注意右边拷贝下来的花哨“水印”）

反正就是感觉设置了重重障碍，不想让大家用 bash。可是越是这样强推 zsh，我就越是怀疑这里面有什么猫腻，越是不想用 zsh。

把系统 shell 改回 bash 之后，发现什么 shell completion，bash 也一样有。要在 prompt 显示 git 的 branch？bash 用几行就能改成方便的形式，也就改个 PS1 变量而已。

parse_git_branch() {

     git branch 2> /dev/null | sed -e ‘/^[^*]/d’ -e ‘s/* \(.*\)/ (\1)/’

}

export PS1=“\[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ ”

所以我发现，之前觉得 zsh 提供的方便东西，本来在 bash 里就都不缺，我有什么理由要用 zsh 呢？我没有理由，所以我就一直用 bash。shell 语言是很差，但我只需要折腾会这一种。我当然不用它写复杂的脚本，写点很短的方便函数就行。对于 *nix 系统，我再也不会考虑使用其它 shell。
