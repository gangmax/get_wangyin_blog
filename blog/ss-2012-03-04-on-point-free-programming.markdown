 [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb531dd6d-b92a-4a1a-8bf2-ea1073566cf9_250x250.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb531dd6d-b92a-4a1a-8bf2-ea1073566cf9_250x250.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb531dd6d-b92a-4a1a-8bf2-ea1073566cf9_250x250.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb531dd6d-b92a-4a1a-8bf2-ea1073566cf9_250x250.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb531dd6d-b92a-4a1a-8bf2-ea1073566cf9_250x250.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb531dd6d-b92a-4a1a-8bf2-ea1073566cf9_250x250.jpeg) 

<span>Concatenative programming, or point-free style, is useful sometimes, but has some serious drawbacks similar to the</span> [SKI combinators](http://en.wikipedia.org/wiki/SKI_combinator_calculus)<span>. Applicative programs can be compiled into point-free style easily, but writing and reading them directly in large scale is usually a mental burden.</span>

It only works well with functions with one or two arguments. Concatenation of functions with more than two arguments will not be so convenient. If the receiver has an argument order that is different from the sender's output order, you will need a non-trivial permutation of argument order.

For example, if the function is defined as:

    f :: Int -> String -> Bool
    f x y = ...

<span>If you want to use it as the predicate for filtering a list of strings, that's fine. You just write something like</span> `filter (f 2) ...`<span>. But what if you want to filter a list of integers? Then you will need to swap the order of the first two arguments before you can do the partial application. So you write</span> `filter (flip f 2) ...`<span>. Fine. But what if the function looks like:</span>

    g :: Int -> A -> String -> Bool
    g x y z = ...

And you want to filter a list of A's? Which function do you use to switch the argument order, and you expect the reader of the program to learn it?

What about functions with four arguments. Notice that there are 4! = 24 different argument orders. How many order switchers do we need?

In order to prevent this kind of plumbing, we have to take unnecessary care when we decide the order of the parameters. This often makes the function look ugly.

Names are more convenient. Notice that even mathematics uses names for permutations (as in algebra):

    (a b c d)
    (b a d c)

Concatenative programming is like connecting the components of a circuit. But even electronic engineers don't do it this way. They use net-lists with names and labels.

Names are essential and useful in most cases. Concatenative programming, although nice when used sparsingly, may not be good to serve as a major way of composition.

At this point, I found this sentence from Tao Te Ching (Chapter 1) especially relevant:

"The nameless is the origin of Heaven and Earth The named is the mother of myriad things"
