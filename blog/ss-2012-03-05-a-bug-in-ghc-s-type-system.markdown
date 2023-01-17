 [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ac463f3-4cfb-4f9b-b834-74006cc0ebed_249x187.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ac463f3-4cfb-4f9b-b834-74006cc0ebed_249x187.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ac463f3-4cfb-4f9b-b834-74006cc0ebed_249x187.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ac463f3-4cfb-4f9b-b834-74006cc0ebed_249x187.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ac463f3-4cfb-4f9b-b834-74006cc0ebed_249x187.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ac463f3-4cfb-4f9b-b834-74006cc0ebed_249x187.jpeg) 

Several days ago, I implemented an experimental type inference system with first-class polymorphism. When comparing it with other systems, I found a possible bug in GHC's type system regarding universal quantification. The phenomemon was confirmed and reproduced by people at #haskell IRC channel for GHC versions above 7.01\. The code that causes trouble is:

> gen :: [forall a. a -> a]
>     gen = [id]
>     test1 = head gen 1

Obviously this program should typecheck, since:

*   `id` <span>has the type</span> `forall a. a -> a`<span>.</span>

*   <span>A list</span> `gen` <span>containing</span> `id` <span>should have type</span> `[forall a. a -> a]`<span>(as in the annotation).</span>

*   `head` <span>has the type</span> `forall a. [a] -> a`<span>.</span>

*   `head gen` <span>should have the type</span> `forall a. a -> a`<span>.</span>

*   `head gen` <span>should be able to be applied to</span> `1`<span>.</span>

But GHC rejected this program for a strange reason.

> Couldn't match expected type `t1 -> t0'
>     with actual type `forall a. a -> a'
>     Expected type: [t1 -> t0]
>     Actual type: [forall a. a -> a]
>     In the first argument of `head', namely `gen'
>     In the expression: head gen 1

On the other hand, it works if (head gen) is bound at let:

> test2 = let hg = head gen in hg 1

It doesn't break the soundness of the type system since it only rejects some correct programs, but this kind of pecularities of type systems can be painful when they add up. I guess this may be caused by the interaction between GHC's internal type system with the legacy let-polymorphism.
