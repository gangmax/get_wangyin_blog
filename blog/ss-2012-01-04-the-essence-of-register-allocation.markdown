# The essence of register allocation

From [here](https://yinwang0.substack.com/p/register-allocation).

[slideshare id=229465411&doc=regalloc-200301034705]

As an independent study project, I designed a new method for register allocation. Different from earlier methods, it departs from the graph coloring formulation and is based on a variation of abstract interpretation which I call "model transformer semantics". I show that register allocation is essentially not a graph coloring problem, but rather similar to a cache replacement or scheduling problem, thus possibly deserves much easier solutions.

<span>I have drafted a paper, but because of other priorities, I don't have time benchmarking it and submitting to a compiler conference. I have put the</span> [full text](http://arxiv.org/abs/1202.5539) <span>to arxiv. I welcome any feedback. I gave a talk about it at Indiana University in Nov 2011.</span>
