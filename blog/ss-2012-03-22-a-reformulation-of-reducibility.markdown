#A reformulation of reducibility

From [here](https://yinwang1.substack.com/p/reducibility).

I found the theory of computation books very imprecise about their descriptions of Turing machines and reductions. They usually start with something precise and mathematical, for example they would define a Turing machine as a 7-tuple, but after that, everything about decidability and reduction is described with impenetrable paragraphs in natural languages.

I believe that the use of natural languages leads to most of the confusion in theory of computation because natural languages are inherently imprecise and ambiguous. There are too many ways to say the same thing. For example, you can find these sentences which mean exactly the same in the books:

*   "Run M on w"

*   "Run M on input w"

*   "Simulate M on w"

The pronouns and references are even more confusing. For example:

> <span>"Use the description of M and w to construct the TM M1</span> _just_ <span>described."</span>

What is "just described", and do M and w here mean the same things as in the earlier paragraph?

Another serious problem is that natural languages are very weak at representing the notion of "interpretation", which underlies much of theory of computation. For example, a Turing machine simulates another Turing machine, which again contains and simulates yet another one.

<span>After some thought, I found that we could use something precise such as mathematical notations combined with programming languages to describe the concepts. As an example, I'll show here how the notion of reduction can be defined precisely as a</span> [homomorphism](http://en.wikipedia.org/wiki/Homomorphism) <span>which can be instantiated for reducing one problem to another.</span>

**Definition 1** <span>(reduction): A</span> _reduction_ <span>(as in theory of computation) is a homomorphism (as in universal algebra):</span>

    Reduce(TM, I) = (TM', I')

satisfying the property

    TM @ I = TM' @ I'

where

*   `TM` <span>= Turing machine which we reduce from</span>

*   `TM'` <span>= Turing machine which we reduce to</span>

*   `I` <span>= input string of TM</span>

*   `I'` <span>= input string of TM'</span>

*   `@` <span>= simulation, similar to the Scheme code</span> `((eval TM) I)`

*   `TM @ I` <span>= result from simulating TM on I (accept or reject)</span>

*   `TM' @ I'` <span>= result from simulating TM' on I' (accept or reject)</span>

End of Definition 1.

<span>Notice that the simulation</span> `(TM @ I)` <span>may go into an infinite loop and never produce any result. Now I show how to use this homomorphism to describe the reduction from ATM ==> HALT, where</span>

*   `ATM` <span>= the "acceptance problem" (deciding whether a Turing machine M accepts string w)</span>

*   `HALT` <span>= the "halting problem" (deciding whether a Turing machine M halts on string w)</span>

For convenience, we let

*   `DATM` <span>= "the decider of ATM"</span>

*   `DHALT` <span>= "the decider of HALT"</span>

Now the reduction can be fully described by the following homomorphism:

    Reduce(DATM, (M,w)) = (DHALT, (M',w))
    where
      M' = <if (M @ w) then accept else loop>
    satisfying
      DATM @ (M,w) = DHALT @ (M',w)

<span>Yes, that's an all-inclusive formal proof that</span> `HALT` <span>is undecidable. It even includes the notion of "reduction" itself.</span>

<span>Let me explain it a bit. The first line says that there exists a function (named</span> `Reduce`<span>) from the pair</span> `(DATM, (M,w))` <span>to another pair</span> `(DHALT, (M',w))`<span>, where</span> `M' = <if (M @ w) then accept else loop>` <span>is a description of a Turing machine.</span>

Now let's look at the last line:

    DATM @ (M,w) = DHALT @ (M',w)

<span>It says: if we have a decider for</span> `HALT` <span>(</span>`DHALT`<span>), then we can use it to define</span> `DATM`<span>, thus deciding</span> `ATM`<span>.</span>

<span>Why this is a valid defintion for</span> `DATM`<span>? This is because from the definition of</span> `M'`

    <if (M @ w) then accept else loop>

we know that:

*   <span>If</span> `(M @ w)` <span>accepts,</span> `M'` <span>accepts, thus</span> `DHALT @ (M',w)` <span>accepts</span>

*   <span>If</span> `(M @ w)` <span>rejects,</span> `M'` <span>loops, thus</span> `DHALT @ (M',w)` <span>rejects</span>

*   <span>If</span> `(M @ w)` <span>loops,</span> `M'` <span>loops, thus</span> `DHALT @ (M',w)` <span>rejects</span>

<span>Notice from the colored words that</span> `DHALT @ (M',w)` <span>will accept if and only if</span> `M` <span>accepts</span> `w`<span>. Thus this defines a decider for</span> `ATM`<span>.</span>

<span>So if</span> `DHALT` <span>exists, then we can have</span> `DATM`<span>. But this contradicts the fact that</span> `DATM` <span>cannot exist, so</span> `DHALT` <span>must not exist.</span>

If you wonder how this proof corresponds to Definition 1, here is some details how it is instantiated:

*   `TM = DATM` <span>(nonexistent)</span>

*   `TM' = DHALT` <span>(hypothetical)</span>

*   `I = (M,w)` <span>where</span> `M` <span>is the description of a Turing machine which we want to know whether it accepts input w.</span>

*   `I' = (M',w)` <span>where</span> `M'` <span>is</span> `<if (M @ w) then accept else loop>`

*   `TM @ I = DATM @ (M,w)` <span>(running decider of</span> `DATM` <span>on input</span> `(M,w)`<span>)</span>

*   `TM @ I' = DHALT @ (M',w)` <span>(running decider of</span> `DHALT` <span>on</span> `(M',w)`<span>)</span>

This is a lot more concise, accurate and easier to understand than a paragraph:

    F = "On input <M,w>:
      1\. Construct the following machine M'
         M' = "On input x:
            1\. Run M on x.
            2\. If M accepts, accept.
            3\. If M rejects, enter a loop."
      2\. Output <M',w>."
