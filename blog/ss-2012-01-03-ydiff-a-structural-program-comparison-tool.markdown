#ydiff: a structural program comparison tool

From [here](https://yinwang1.substack.com/p/ydiff).

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F99981bfc-9a10-4513-8b94-cb1f5aef9d0b_300x210.gif)

(Click on the above picture to see it in action. See the end of the post for more demos)

## Motivation

<span>I have been imagining a world where programs are not represented as text, but as data structures. They will be edited not with text editors, but with</span> _structural editors_<span>, which create and manipulate the abstract syntax trees (AST) directly. In such a programming environment, the line-by-line diff utilities and version control tools will stop working, because there are no longer "lines" or "words" in programs.</span>

ydiff is a proof-of-concept for handling this situation. It is a diff tool designed for "structural programming".

Currently ydiff takes pains to parse program text into ASTs, but hopefully in the future programs will be stored directly as data structures so that the parsing step can be skipped. This will enable this kind of tool to extend to all programming languages effortlessly.

## Features

*   **Language-aware**<span>. ydiff parses programs, understands basic language constructs and will not make non-sensical comparisons. For example it will not compare a string "10000" with an integer 10000 even though they look very similar. Also, it tries to match functions with the same name before it attempts to destruct and compare functions of different names.</span>

*   **Format insensitive**<span>. The comparison result will not be affected by different number of white spaces, line breaks or indentation. For example, ydiff will not produce a large diff just because you surrounded a block of code with if (condition) {...}.</span>

*   **Moved code detection**<span>. ydiff can find refactored code -- renamed, moved, reordered, wrapped, lifted, combined or fragmented code. Refactored code can be detected however deep they are into the structures.</span>

*   **Human-friendly output**<span>. The output of ydiff is designed for human understanding. The interactive UI helps the user navigate and understand changes efficiently.</span>

<span>These properties make ydiff helpful for understanding changes. It may also be possibly used for detecting plagiarism in programming classes or copyright infringement of code. For large-scale use cases you may be more interested in</span> [MOSS](http://theory.stanford.edu/~aiken/moss)<span>, but ydiff is fundamentally more accurate because it parses programs.</span>

## Demos

Here are some interactive HTML demos with a pretty nice UI design. The left and right windows are always locked in their relative position. A mouse click on changed, moved or unchanged nodes will highlight the matched nodes and scroll the other window to match. After that, the windows will be locked into their new relative position for browsing.

Okay, here are the demos.

*   [Scheme Demo1](http://www.yinwang.org/resources/diff1-diff2.html)<span>. ydiff's algorithm diffing itself (between the first version on GitHub and the latest version).</span>

*   [Scheme Demo 2](http://www.yinwang.org/resources/mk1-mk2.html)<span>. Comparison of the original</span> [miniKanren](http://code.google.com/p/iucs-relational-research) <span>from Professor Dan Friendman and the version I modified in order to support</span> _condc_<span>, a "negation operator". Pay attention to the function</span> `unify`<span>, whose major part is moved into</span> `unify-good`<span>.</span>

*   [Emacs Lisp](http://www.yinwang.org/resources/paredit20-paredit23.html)<span>. Comparison of two versions (v20 and v23) of Taylor Campbell's</span> [paredit-mode](http://mumble.net/~campbell/emacs/paredit.el)<span>, a structural editing mode of emacs for Lisp programs.</span>

*   [Clojure](http://www.yinwang.org/resources/typed-clojure1-typed-clojure2.html)<span>. Compare the first commit of</span> [Typed Clojure](https://github.com/clojure/core.typed/blob/master/src/main/clojure/clojure/core/typed.clj) <span>with its recent version.</span>

*   [Arbitrary S-expressions](http://www.cs.indiana.edu/~yw21/demos/pass1-pass2.html)<span>. Trying to find a bug in an optimizing pass of my Scheme compiler by comparing the IRs (represented as S-expressions).</span>

*   [Python](http://www.cs.indiana.edu/~yw21/demos/demo1-demo2.html)<span>. ydiff has a completely separate implementation in Python (named "PyDiff"), which can diff two Python programs. This is a comparison of two implementations of a small list library that I wrote, which implements Lisp-style lists. The first implementation uses recursive procedures while the second uses Python's generator syntax and is iterative. Pay some attention to</span> `append`<span>, whose code is moved inside another function</span> `appendAll`<span>.</span>

*   [Javascript](http://www.yinwang.org/resources/nav1-nav2.html)<span>. Comparison between two major revisions of the UI code of ydiff itself.</span>

*   [C++ demo1](http://www.yinwang.org/resources/d8-3404-d8-8424.html) <span>and</span> [C++ demo2](http://www.yinwang.org/resources/simulator-mips-simulator-arm.html)<span>. There are two demos for C++. The first demo compares two versions of the d8 Javascript debugger from the</span> [V8 project](http://v8.googlecode.com)<span>(v3404 from 2009 and v8424 from 2011). The second demo compares V8's simulators for two different processors (MIPS and ARM).The d8 demo is especially interesting because by clicking on the lines of the method</span> `Shell::Initialize`<span>in the old version, it can be clearly observed that its body has been distributed into several procedures in the new version:</span>

        Shell::Initialize
        Shell::CreateGlobalTemplate
        Shell::RenewEvaluationContext
        Shell::InstallUtilityScript

    <span>Also the major part of</span> `Shell::Main` <span>is moved into the helper</span> `Shell::RunMain`<span>.</span>

## Get the code

<span>ydiff is an open source project. You can follow its development on github:</span> [yinwang0/ydiff](http://github.com/yinwang0/ydiff) <span>or get its source code from there.</span>
