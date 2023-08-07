# Sum types and union types

From [here](https://yinwang1.substack.com/p/sum).

In a new type system I'm designing, I was trying to find a good reason to get rid of sum types (as are commonly used in ML and Haskell). Well, I don't hate them that much, but for simplicity's sake, I always try to remove things unless there are undeniable reasons that they must exist.

I think sum types have a large overlapping of functionality with product types and cause inelegance and inefficiency, so I hope to replace them with union types (some people call "open unions"). Union types are more orthogonal with respect to product types. I seem to have found a good idea where sum types originated and the reason why we don't need them in a programming language.

<span>It appears that sum types were originated from mathematics. In mathematics, there are no</span> _named_ <span>product types. All we have are Cartesian products. Cartesian products have no constructors (or type tags) in them. How do we distinguish a</span> _student_ <span>represented as (Height x Weight) with a</span> _professor_<span>, also represented as (Height x Weight)? We put tags on them before putting them into a</span> _disjoint union_<span>. This process is called</span> _injection_<span>. We do this every time when putting something into a disjoint union, and we</span> _project_ <span>the elements out when we need their values.</span>

From a programming point of view, the injections and projections are inefficient and inconvenient. This is equivalent to constructing new objects whenever we need to put them into a list, and destructing them when we need their components. Then construct new objects (again) when we need to put them into another list, and so on.

<span>In order to avoid these shortcomings, programming language researchers decided to attach type tags to the objects when they are created. The tags tell us what the object is and they stay with the objects throughout their life-time. This results in</span> _record_ <span>types. But somehow the PL researchers seemed to haven't been completely freed from the influence of mathematics. They decided that each variant of a union needs to define a new constructor (injection). Thus sum types were born. For example,</span>

    data T1 = Foo Int | Bar String

<span>Here</span> `Foo` <span>and</span> `Bar` <span>are essentially injections. Why do we need the injections and projections in a language where type tags always tell us what an object is? Another problem is that a constructor can only belong to one sum type, and there is no way we can reuse it in another. For example, there is no way you can define another sum type like:</span>

    data T2 = Foo Bool | Baz Float

<span>because</span> `Foo` <span>is already defined in</span> `T1`<span>. What we wanted to express is that Foo belongs to the union T1 and it also belongs to the union T2\. This is a very reasonable need, but most Hindley-Milner style type systems doesn't allow this.</span>

If we relax the requirement that each variant of a sum type must define a new constructor, we get union types. They are more general and orthogonal with respect to product types. We can always choose to put another level of type tags upon the variants, therefore we lose nothing if we don't have sum types.
