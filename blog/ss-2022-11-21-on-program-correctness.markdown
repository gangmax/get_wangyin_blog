# On Program Correctness

From [here](https://yinwang0.substack.com/p/on-program-correctness).

No matter in the academic circle or in the industrial circle, there are always many people who care too much about the so-called "correctness of the program", and some even go to the point of trembling and chasing after the end. Here are a few examples:

Many people take testing (test) too seriously. Before the horoscope of the code was written, I was clamoring for how to test it strictly to prevent someone from changing the code wrong in the "future". These people are often bound by the test in the end, unable to move an inch. Not only is the code full of bugs, but there are also many bugs in the test.

Some people care too much about the question of "what language to use", as if they can only complete some very basic tasks with the latest, coolest and most functional language. This kind of person sees some new language as a "panacea" time and time again, and then becomes disillusioned again and again, and finally they don't write any useful code.

Some people pay too much attention to the so-called "type safety", and often complain that the language at hand lacks some cool type system functions, and even say that it is impossible to write code because of this! What they don't see is that even without some type safety guaranteed statically by the compiler, the code is perfectly fine and perhaps simpler.

Some people go to the extreme and think that all code must use so-called "formal methods" (formal methods), using machine theorem proofs to ensure that it is 100% error-free. This kind of person is so happy to prove toy-sized code that he never writes code that solves a real problem in his life.

100% reliable code, what a perfect ideal! But in the end, you find that people who talk about "correctness" and "reliability" every day are almost always high-minded, and they talk more than they do. I haven't written any code to solve practical problems, but I like to comment on other people's "code quality". These people's own codes are often extremely complicated, and they like to use various seemingly sophisticated tricks to ensure the so-called "correctness". Their code is tied up with many so-called "testing tools" and "type systems", but it is still full of bugs. Later, you gradually discovered that the fear of "correctness" is actually an excuse for these people not to solve the problem at hand.

The most important criteria for measuring the program

These people actually don't understand an important truth: you have to write the program before you can start talking about its correctness. Whether a program is good or not, the most important criterion is whether it can effectively solve the problem, not whether it is correct. If your program doesn't solve a problem, or solves the wrong problem, or solves a problem but is very difficult to use, then no matter how correct or reliable your program is, it is not a good program.

Correctness is not the same as simplicity, elegance, or efficiency. A program that isn't simple, elegant, or efficient, and even if you've gone to great lengths to prove it correct, it still won't work well. It's like you have to have a house before you can start asking it to be safe. Think about it, if a homeless man without a house passes by a house that no one lives in, will he continue to eat and sleep in the wild because the house is "not 100% safe"? Writing code is like having a house, and the correctness of the code is like the security of the house. Writing programs that can solve problems is always the first priority. And the correctness of this program, no matter how important it is, will always be secondary. The emphasis on program correctness should never be higher than writing the program itself.

Whenever I talk about this issue, I like to make an analogy: If the "Riemann Hypothesis" is proved by Wang Yin, will it be renamed "Wang Yin's Theorem"? of course not. It will be called "Riemann's Theorem"! This is because, no matter how smart or powerful a person is, even if he can prove the Riemann conjecture, this conjecture is not the first one he came up with. If Riemann hadn't proposed this conjecture, you wouldn't have thought of it at all, so how can you talk about proof? So I like to say that first-rate mathematicians propose conjectures, and second-rate mathematicians prove other people's conjectures. By the same token, the person who writes the code that solves the problem is always more important than the person who proves (tests) the correctness of his code. Because if he hadn't written this code, you wouldn't even know what to prove (test)!

How to improve the correctness of the program

Having said that, although the correctness of the program is relatively secondary to solving the problem, it cannot be ignored. But this does not mean that advocating "testing" and "formal proof" every day can improve the correctness of the program.

If you have studied the logical derivation of the program in depth, you will know that the ability to test and formally prove is very limited. Tests can only test the most commonly used cases, but cannot cover all cases. Don't be fooled by the so-called "test coverage". Just because a line of code is covered by tests without errors does not mean that there will be no errors there. Whether a line of code is wrong depends on all the conditions that pass before it runs. The number of these conditions is a combinatorial explosion, and basically no test can cover all of these preconditions.

Formal methods are effective for very simple and straightforward programs, but once the program is a little bit larger, formal methods fail. You may not have thought that you can write a mathematical conjecture such as Collatz Conjecture that has not been proven so far with very little code. The code in actual use is many times more complicated than this mathematical conjecture. You have to use formal methods to prove all the code, which basically means that you will never be able to complete the project.

So what is the most effective way to improve program correctness? In my opinion, the most effective way is to think and scrutinize the code to make it simple and intuitive, until you can see at a glance that there is no problem with it.

<span>(Translated from Chinese blog 《</span>[谈程序的正确性](http://www.yinwang.org/blog-cn/2015/07/02/program-correctness)<span>》)</span>
