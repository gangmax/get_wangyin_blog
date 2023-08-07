# Propositions as Programs

From [here](https://yinwang1.substack.com/p/propositions-as-programs).

<span>The</span> [Curry-Howard correspondence](http://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence) <span>says that propositions are types and proofs are programs. I had been wondering if there is a simpler way to think about it, so I came up with this:</span>

> <span>Propositions are programs; proofs are "abstract interpretation" of them to</span> `True`<span>.</span>

<span>Here</span> `True` <span>is a meta-level truth value. A theorem prover is then an</span> _abstract interpreter_ <span>which tries to evaluate the proposition to</span> `True`<span>. This computational process which derives</span> `True` <span>from the proposition is called a</span> _judgment_<span>.</span>

<span>Here I may have conflated the concept of abstract interpretation. I choose to use this term just because those two words "abstract" and "interpretation" convey the general idea that I hope to capture, but the term</span> _abstract interpretation_ <span>here may not be what you used to think it is. I could have used</span> _supercompilation_<span>, but I don't think the word grasps the concept very well.</span>

<span>Anyway, this is a special kind of evaluation. It may be called</span> _partial evaluation_<span>,</span> _supercompilation_<span>, or some sort of</span> _static analysis_<span>, whatever you call it. It can also take human inputs interactively, as long as it is semantic-preserving -- it returns</span> `True` <span>whenever an actual interpreter would return</span> `True`<span>. But it is a lot more efficient because unlike normal interpreters, it takes shortcuts (induction hypotheses). If the program thus evaluates to</span> `True`<span>, then the proposition is proved.</span>

<span>This is much like fortune-telling. It quickly tells you the result that an actual interpreter would eventually give you after some time. It has a limited number of basic reduction operations such as</span> _unfolding_<span>,</span> _induction_ <span>and</span> _rewriting_<span>, so we can record the reduction sequences as</span> _proofs_<span>, and we can verify them later on.</span>

This seems to match what we have been doing with proof assistants like Coq. Comparing with Curry-Howard correspondence, this is possibly a more natural way of thinking about theorem proving.

The propositions in Coq are a little far-fetched to be called "types" of the proof terms. For example, we can have a proof term like

    fun (n' : nat) (IHn' : n' + 0 = n') => ...

<span>Is</span> `n' + 0 = n'` <span>the type of</span> `IHn'`<span>? Well, you have the freedom to call it a type, but this doesn't feel natural. What we want is just a way to</span> _bind_ <span>an equation to a name, so that we can refer to it later. The semantics of type annotations, for example</span> `IHn' : n' + 0 = n'` <span>here, happen to make the required binding for us.</span>

<span>It feels better if we just think of propositions as programs with boolean return types, and think of the proof terms reduction sequences of them into</span> `True`<span>. If you take a look at the proof terms of Coq, you may find that this is the case. For example, take a look at this simple theorem and the tactics that prove it:</span>

    Theorem plus_0_r : forall n : nat, n + 0 = n.
    Proof.
      intros n. induction n as [| n'].
      reflexivity.
      simpl. rewrite -> IHn'. reflexivity.  Qed.

They produce the following proof term:

    plus_0_r = 
    fun n : nat =>
    nat_ind (fun n0 : nat => n0 + 0 = n0) eq_refl
      (fun (n' : nat) (IHn' : n' + 0 = n') =>
       eq_ind_r (fun n0 : nat => S n0 = S n') eq_refl IHn') n
         : forall n : nat, n + 0 = n

<span>You may think of this proof term as a program with the theorem as its type, but you can also think of it as a</span> _reduction sequence_ <span>of the program</span> `n + 0 = n` <span>to</span> `True`<span>, where</span> `n` <span>is a natural number. It is saying: "Do an induction where the first branch executes an equivalence judgment, and the other branch does an unfolding, a rewriting using the induction hypothesis, and an equivalence judgment." I think this way of thinking is much more natural.</span>

This interpretation can also explain the operation of Boyer-Moore style theorem provers (ACL2), as this is almost exactly how they work.

You may have noticed that we have an important difference from the original Curry-Howard correspondence here:

> Proofs are no longer considered programs.

At least proofs are not object-level programs. They are just reduction sequences in the abstract interpreter, which are at the meta-level. We can give this reduction sequence to an independent verifier so that it can replay the abstract interpretation and verify the correctness of the proof.

<span>Alternatively, if you consider the verifier as an interpreter, then proofs are its input programs. In this sense, you can also say that</span> _proofs are programs for the proof verifier_<span>, and both propositions and proofs can be considered programs. But they are programs at two different semantic levels: the proofs are at a higher level than the propositions. This is quite different from Curry-Howard correspondence.</span>

Thus, we have arrived at a unified way of thinking about two very different styles of theorem proving: Curry-Howard correspondence (as in Coq), and Boyer-Moore (as in ACL2).
