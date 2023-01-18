# PySonar: a type inferencer and indexer for Python

From [here](https://yinwang0.substack.com/p/pysonar).

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F39ac9350-362b-4419-ad84-33e4adfe1798_500x384.gif "pysonar2")

PySonar is a type inferencer and indexer for Python. It includes a powerful type system and a sophisticated inter-procedural analysis. Compared to style-checking tools or IDEs, PySonar analyzes programs in deeper ways and produces more accurate results. PySonar resolves more names than typical IDEs. The current resolution rate is about 97% for Python's standard library.

### Demos

<span>To get a quick feel about what PySonar can do, here is a </span>[sample analysis result](http://www.yinwang.org/resources/demos/pysonar2/email/header.py.html)<span> for a small fraction of Python's standard library.</span>

### What's in there

1.  **A powerful type system. **<span>In addition to the usual types you can find in programming languages, PySonar's type system has </span>_union types_<span>and</span> _intersection types -- _<span>two of the most powerful elements I have found during my PL research. They are rarely found in programming languages. I know of only two languages with statically checked union types:</span> [Typed Racket](http://docs.racket-lang.org/ts-guide/beginning.html#%28part._.Datatypes_and_.Unions%29)<span> and </span>[Ceylon](http://ceylon-lang.org/documentation/1.0/tour/types)<span>. Different from these languages, PySonar can work without any type annotations. It infers all the types by doing inter-procedural analysis.</span>

2.  **Control-flow aware interprocedural analysis**<span>. Because Python has very dynamic and polymorphic semantics and doesn't contain type annotations, a modular type inference system such as the</span> [Hindley-Milner system](http://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system) <span>will not work. I actually implemented a HM-like system in the first version of PySonar, but it didn't work well. As a consequence, all types are inferred by an inter-procedural analysis which follows the control-flow and some other aspects of the semantics.</span>

3.  **Handling of Python's dynamism. **<span>Static analysis for Python is hard because it has many dynamic features. They help make programs concise and flexible, but they also make automated reasoning about Python programs hard. Some of these features can be reasonably handled but some others not. For code that are undecidable, PySonar attempts to report all known possibilities. For example, it can infer union types which contains all possible types it can possibly have:</span>

4.  **High accuracy semantic indexing** <span>PySonar can build code indexes that respects scopes and types. Because it performs inter-procedural analysis, it is often able to find the definitions of attributes inside function parameters. This works across functions, classes and modules. The following image shows that it can accurately locate the field</span> `x.z` <span>which refers to the "z" fields in classes</span> `B1` <span>and</span> `C1`<span>, but not</span> `A1`<span>.</span>

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2eb28281-71c7-47c9-879f-1e6e6a9f52dc_654x367.png)

### Availability

<span>The code is open source from my</span> [GitHub repository](https://github.com/yinwang0)<span>.</span>

### Users

Here are some of PySonar's users:

*   **Google**<span>. Google uses PySonar 1.0 to index millions of lines of Python code, serving internal code search and analysis services such as Grok and Code Search</span>

*   **[SourceGraph](http://www.sourcegraph.com)**<span>. SourceGraph is a semantic code search engine. They use PySonar to index hundreds of thousands of opensource Python repositories. They started using PySonar 1.0 as the Python analysis for their site. I recently joined them and finished integrating PySonar 2.0</span>
