# ADTs and objects

From [here](https://yinwang0.substack.com/p/objects).

<span>After reading William Cook's essay</span> _[On Understanding Data Abstraction, Revisited](http://www.cs.utexas.edu/~wcook/Drafts/2009/essay.pdf)_<span>, let me try to condense the difference between abstract data types (ADTs) and objects into a few words.</span>

(To avoid ambiguity, I use "instances" to stand for data created by instantiating ADTs)

*   "Instances" created by the same ADT share the same functions (methods). Functions may be parameterized, but the code is the same in each instance. Because of this, they need to share the same representation.

*   "Objects" (as proposed by Cook) don't necessarily share function code. Each object may have a completely different set of functions (with matching names and types). This is in essence the same as "call-backs" in GUI widgets. Because of this diversity, each object may have completely different representation.

Ironically, it is usually the former case in mainstream object-oriented languages like Java and C++. In Java you can somehow achieve the latter with interfaces and anonymous classes, but it is awkward. JavaScript's prototype-based system seems to be closer to the essence of the latter, but still not feel natural.

But different from Cook's view, I think it is better not to consider binary operations like set union as methods. Union may take two sets with different representations and create a new one, thus it can operate by using the "true methods" of both arguments (possibly iterators and membership).
