# Purely Functional Languages and Monads

From [here](https://yinwang1.substack.com/p/pure-fp-and-monads).

In general, functional languages are pleasant to work with because they support first-class functions, which are a very powerful modeling tool. But if you pursue the extreme---to use a purely functional language, you get adverse effects similar to OO design patterns.

In a conventional OO language, having to use OO design patterns makes hard things even harder; but in a purely functional language, having to use pure functions to model side-effects makes trivial things hard and hard things impossible. So speaking of the two evils, OOP is the lesser one because at least easy things are still easy in them.

The problem with pure FP is: there exists things that are not pure.

### Side-effects are real

Electrical engineers probably have the best understanding of purely functional languages, because electric wires are pure by default (if you are not paranoid enough to count heat as a side-effect). Purely functional languages are the analogous of combinational logic circuits.

<span>Combinational logic circuits are very useful and are an important part of a system, but you can't use them alone to build up complex systems. This is why people invented flip-flops and sequential logic circuits. If you look at the design of the flip-flops, you will start to appreciate the ingenuity in them. They create </span>_memory_ <span>out of pure circuits. Memory is where side-effects come from.</span>

<span>So pureness comes for free, but side-effects took efforts to invent. Unfortunately a large portion of the physical capabilities provided by the sequential circuits are disregarded by purely functional languages. Instead, purely functional languages are obsessed in simulating the effects on their own. There is a difference between the </span>_physical_<span> and the </span>_simulated_<span>. The simulated can't be as efficient as the physical.</span>

For a simple example, many efficient data structures rely on mutations to create connections between their components (think about circular data structures and networks). In such structures, side-effects act very much like a physical force to hold the parts together, and update them as needed.

To implement this in a purely functional language, you have to use indirect ways. Every time you change it, you need to create a new data structure which shares most of the old data structure. But then you got into the trouble of keeping track of where the "current structure" is. It is moving in the dataflow and you have to carefully pass it on. Had you used side-effects, the structure can stay at the same location, so you won't need to worry losing track of it. You don't need to pass it on. This will save lots of administrative code.

Also, sharing the old structures induces extra levels of indirection in the data structure, which causes significant overhead. Thus purely functional data structures can't really match the performance provided by its impure counterpart. Purely functional data structures also cause lots of object creation and thus stress the garbage collector.

<span>Some people say that purely functional data structures will reduce contention when there is lots of concurrency, but notice that if the observers of the</span> _old_ <span>data structure "purely update" it, they will hold a</span> _different_ <span>structure other than it's current state. After that point, the universe is "forked" and they will live in completely different worlds. You will lose consistency.</span>

If you really want all threads to see the same data structure, then the contention is unavoidable, because you need a channel for the information to pass through. Nothing can save you from the contention because there is data dependency.

Everything is persistent in purely functional data structures, but how often do you need the outdated ones? In impure data structures, you still have the choice of making copies when necessary and achieve the same persistence effect, just with better performance.

### Monads are design patterns

Purely functional languages also complicates the programs and ensue a huge cognitive cost. Modeling side-effects using pure functions is in the same mentality of wrapping functions inside objects as in OOP. They are both over-engineering and cause unnecessary manual labor.

<span>One of the major design patterns in purely functional languages is called</span> _monads_<span>, a highly stylized way of structuring side-effects. If you look deep into them, monads make programs complicated and hard to write, and monad transformers are in essence a hack to get around monads' limitations---they are not principled ways of composing monads. Representing side-effects using monads is as convoluted as writing interpreters or compilers using visitor patterns. For this matter, I wrote a</span> [short article](http://yinwang0.wordpress.com/2013/03/31/purely-functional) <span>some time ago which not many people have read:</span>

> <span>To write programs in a purely functional programming language is much like living in a </span>_wired world_<span>. In such a world, there are no electromagnetic waves nor sound waves, so you don’t have wifi, cell phones, satellite TV, radios, etc. You don’t even have light or sound. In other words, everything is blind and deaf.</span>
> 
> All information must pass through wires or pipes, connected by switch boxes which we call “monads”. You must carefully route all the wires and pipes and connect them correctly before any information processing device, including your eyes and ears, can properly work.

<span>Trivial things in other languages (such as random number generators or circular data structures) become non-trivial in a purely functional language. Easy things often become research problems when you try to write them using monads, so you often see papers titled</span> _A Monadic Approach to a-solved-problem_<span>.</span>

<span>About this I have an interesting story to tell. Once upon a time, my PhD advisor Amr Sabry tried to reimplement Dan Friedman's </span>[miniKanren](http://minikanren.org/) <span>(a logic programming language) in Haskell, but he couldn't figure out how to compose the monads. He asked for help from Oleg Kiselyov, arguably the world's most knowledgeable person about getting around Haskell's type system.</span>

<span>And if you don't know, Amr Sabry is probably the world's most knowledgeable person about purely functional programming languages and side-effects. His paper </span>_[What is a Purely Functional Language](http://www.cs.indiana.edu/~sabry/papers/purelyFunctional.ps)_<span> is often referred to as the official definition of "pureness". After solving the problem with Oleg's help, they coauthored a Functional Pearl </span>[paper](http://okmij.org/ftp/Computation/monads.html#LogicT)<span>.</span>

Ironically, Dan Friedman, the original author of that piece of code, didn't have any such trouble writing it in Scheme in the first place. Certainly there is no reason Amr should be able to figure out how to compose the monads. He and Oleg just wrote the Haskell code for fun, but this story tells me something about monads: they make things unnecessarily complicated.

How did Dan Friedman write the code so easily? He just directly passed the states in-and-out and not using any monads, or you can say that he used monads' essence without actually using them.

Following Dan's style, I rewrote miniKanren, added constraint logic programming to it. All this is done within three weeks during my first semester as a PhD student, together with Dan's B521, Amr's B522, other course loads and teaching duties. I would certainly be bogged down had I used monads, and I don't see any point of translating it into a monadic style. It is just so much simpler without monads.

<span>(</span>_Correction to some historical facts by request from Prof. Friedman_<span>: He'd like to give a lot of the credits of the current miniKanren code's simplicity to Chung-Chieh Shan, who at one moment simplified the code to its current style.)</span>

### Equational reasoning can't save the world

<span>On the safety side, purely functional languages haven't much advantage either. Some people claim that the value of monads is that they explicitly delimit the side-effects and support equational reasoning, but programs are not always as easy as algebra formulas such as a</span>_(b+c)=a_<span>b+a*c. If all programs are that easy, we would not need monads at all. Monads don't really make your program easier to reason about.</span>

Pure functions always return the same results when they are given the same input, but every monadic function has an extra "implicit" argument which is different at every call to the same function, so although it is still true that "pure functions always return the same results when they are given the same input", the problem is, you never get the same input because of that always-changing extra argument! You don't know what's inside that argument. That argument is called the "state".

There is no way you can statically know the values inside state monads, for the same reason that you don't know the values inside the heap. This is because the state monads are in essence the same as the heap. The heap maps memory addresses to values, and state monads map variables to values.

If you have written static analysis, it will be clear that monadic code is in essence putting parts of a static analysis into the user's code. In other words, every monadic code is reimplementing part of a static analysis. So monadic code is as hard to analyze as if you use side-effects, only that it takes a lot more work to write.

You can write horribly side-effective code with monads which nobody can understand and no static analysis tool can help. There is no such thing monads can make easier which can't be done by static analysis.

### You can write pure functions in any language

Monads are contagious. Once the code gets into monads, it is not easy to get out. Having to explicitly specify side-effects in the types is similar to having to explicitly declare exceptions in Java. You must either "handle" it, or you must declare that you have passed it on. Why should programmers write them while they can be easily inferred by static analysis? Static analysis use what is essentially monads (or even more advanced techniques), and they take the burden of writing monadic code away from programmers.

Of course overusing side-effects will make programs harder to analyze, but you can reduce side-effects and write pure functions even in an impure language. For example, the following C function is a pure function, satisfying every requirement of the definition of "pureness".

[code language="c"] int f(int x) { int y = 0; int z = 0; y = 2 * x; z = y + 1; return z / 3; } [/code]

Advanced static analysis tools would have no trouble figuring out things about this kind of code. They would know that this function is pure without you writing any annotations, and they can do a lot more for you than this. So pure functions don't just belong to purely functional languages. You can write pure functions in any language (including assembly), but the point is, you should be allowed to use side-effects too, especially when they make things easier.

### Thinking critically about mathematics as a language

Looking back into history, the dogma from mathematics is the driving force behind purely functional languages. Mathematical functions are simple and beautiful, but unfortunately they work well only when the thing you are trying to model is pure by nature. Purely functional language proponents like using buzzwords like "category theory", and call those who don't understand it "uninitiated".

I know a considerable amount of category theory. Even the category theorists themselves call it "abstract nonsense", because it is to a large extent a grotesque way of saying what other mathematicians already know, in much the same sense that GoF design patterns are a grotesque way of saying what most decent programmers already know. So category theory is the analogous of design patterns in mathematics.

<span>If you read Gottlob Frege's article </span>_[Function and concept](http://www.olimon.org/uan/frege-writings.pdf)<span>, </span>_<span>you will be surprised that most mathematicians got functions wrong before his writing, and that was just a little more than a hundred years ago. Mathematics have done lots of things wrong with its language. This has been pointed out a long time ago by Gerald Susman in his</span> [Structure and Interpretation of Classical Mechanics](http://mitpress.mit.edu/sites/default/files/titles/content/sicm/book.html)<span>and recently in his</span> [InfoQ talk](http://www.infoq.com/presentations/Expression-of-Ideas)<span>. There is a lot of truth in his words.</span>

There is no reason programming language designers should blindly follow the ways of mathematics, because it is just another quirky language.

### What is functional programming, really?

The above is not to disagree with functional programming in general. On the contrary, functional programming in general is highly valued. I just disagree with the dogma of the "purely functional" ones. Impure functional languages such as Scheme and ML haven't these problems. They have "benign side-effects". In fact, in Scheme functions are called "procedures", not "functions". This is because its designers know that they are not functions in the mathematical sense, and they intended to make them not necessarily pure.

<span>The purely functional language community often try to steal the word "functional programming" from traditional functional languages (Lisp, Scheme, ML), as if only </span>_purely_ <span>functional languages deserve the name. This is not fair. We should be able to use the word "functional programming language" to refer to any language with correct implementation of first-class functions.</span>

### Don't fall in love with your model

Everything starts to do harm when they are pursued to the extreme. Purely functional programming tries to fit the world into its model, but the world works in its own ways. It is wrong to think of everything as a nail when you have a hammer. Only by observing the reality can we get out of the religions that are limiting us. Don't fit the world to your model. Fit your model to the world.
