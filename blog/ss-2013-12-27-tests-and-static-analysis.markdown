# Tests and static analysis

From [here](https://yinwang1.substack.com/p/tests-and-static-anaysis).

<span>Ever since I made a static analysis tool for Python called</span> [PySonar](http://yinwang0.wordpress.com/2010/09/12/pysonar)<span>, I have been asked about the question: "What is the difference between testing and static analysis?" When I worked at</span> [Coverity](http://www.coverity.com)<span>, my coworkers told me that they also spent quite some time explaining to people about their difference. My answer to this question evolves as my understanding of this area deepens. Recently I replied to a comment asking a similar question, so I think it's a good time to write down some systematic answer for this question.</span>

### Static analysis is static, tests are dynamic

Static analysis and tests are similar in their purposes. They are both tools for improving code quality. But they are very different in nature: static analysis is (of course) static, but tests are dynamic. "Static" basically means "without running the program".

Static analysis is similar to the compiler's type checker but usually a lot more powerful. Static analysis finds more than type errors. It can find defects such as resource leaks, array index out of bounds, security risks etc. Advanced static analysis tools may contain some capabilities of an automatic theorem prover. In essence a type checker can be considered a static analysis with a coarse precision.

Static analysis is like predicting the future, but testing is like doing small experiments in real life. Static analysis has the “reasoning power” that tests hasn't, so static analysis can find problems that tests may never detect. For example, a security static analysis may show you how your website can be hacked after a series of events that you may never thought of.

On the other hand, tests just run the programs with certain inputs. They are fully dynamic, so you can't test all cases but just some of them. But because tests run dynamically, they may detect bugs that static analysis can't find. For example, tests may find that your autopilot program produces wrong results at certain altitude and speed. Static analysis tools can't check this kind of complex dynamic properties because they don't have access to the actual running situation.

<span>But notice that although tests can tell you that your algorithm is wrong, they can't tell you that it is</span> _correct_<span>. To guarantee the correctness of programs is terribly harder than tests or static analysis. You need a mechanical proof of the program's correctness, which means at the moment that you need a theorem prover (or proof assistant) such as Coq, Isabelle or ACL2, lots of knowledge of math and logic, lots of experience dealing with those tools' quirks, lots of time, and even with all those you may not be able to prove it, because you program can easily encode something like the</span> [Collatz conjecture](http://en.wikipedia.org/wiki/Collatz_conjecture) <span>in it. So the program's passing the tests doesn't mean it is correct. It only means that you haven't done terribly stupid things.</span>

### Difference in manual labor

<span>Testing requires lots of manual work. Tests for "silly bugs" (such as null pointer dereference) are very boring and tedious to make. Because of the</span> [design flaws](http://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare) <span>of lots of programming languages, those things can happen anywhere in the code, so you need a good coverage in order to prevent them.</span>

<span>You can't just make sure that every</span> _line_ <span>of the code is covered by the tests, you need good</span>[path coverage](http://homepage.hispeed.ch/pjcj/testing_and_code_coverage/paper.html#path_coverage)<span>. But in the worst case, the number of execution paths of the program is exponential to its size, so it is almost impossible to get good path coverage however careful you are.</span>

On the other hand, static analysis is fully automatic. It explores all paths in the program systematically, so you get very high path coverage for free. Because of the exponential algorithm complexity exploring the paths, static analysis tools may use some heuristics to cut down running time, so the coverage may not be 100%, but it's still enormously higher than any human test writer can get.

### Static analysis is symbolic

<span>Even when you get good path coverage in tests, you may still miss lots of bugs. Because you can only pass specific values into the tests, the code can still crash at the values that you haven’t tested. In comparison, static analysis processes the code</span> _symbolically._<span>It doesn’t assume specific values for variables. It reasons about</span> _all_ <span>possible values for every variable. This is a bit like computer algebra systems (e.g. Mathematica) although it doesn't do sophisticated math.</span>

The most powerful static analysis tools can keep track of specific ranges of the numbers that the variables represent, so they may statically detect bugs such as "array index out of bound" etc. Tests may detect those bugs too, but only if you pass them specific values that hits the boundary conditions. Those tests are painful to make, because the indexes may come after a series of arithmetic operations. You will have a hard time finding the cases where the final result can hit the boundary.

### Static analysis has false positives

<span>Some static analysis tools may be designed to be conservative. That is, whenever it is unsure, it can assume that the worst things can happen and issue a warning: "You may have a problem here." Thus in principle it can tell you whenever some code </span>_may_ <span>cause trouble. But a lot of times the bugs may never happen, this is called a</span>_false positive_<span>. This is like your doctor misdiagnosed you to have some disease which you don't have. Lots of the work in building static analysis tools is about how to reduce the false positive rate, so that the users don't lose faith in the diagnosis reports.</span>

Tests don't have false positives, because when they fail your program will surely fail under those conditions.

### The value of static analysis

Although static analysis tools don't have the power to guarantee the correctness of programs, they are the most powerful bug-finding tools that don't need lots of manual labor. They can prevent lots of the silly bugs that we spend a lot of time and energy writing tests for. Some of those bugs are stupid but very easy to make. Once they happen they may crash an airplane or launch a missile. So static analysis is a very useful and valuable tool. It takes over the mindless and tedious jobs from human testers so that they can focus on more intellectual and interesting tests.
