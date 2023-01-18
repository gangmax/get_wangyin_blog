# Why is indexing faster than binary search

From [here](https://yinwang0.substack.com/p/indexing).

We all know that indexing into an array takes only O(1) time, while searching for a number in a sorted array takes O(n) time with linear search, and O(log n) time with binary search. But why is indexing so fast? What is the secret sauce?

The reason is really about the nature of indexing -- how it is implemented in a circuit. In order to illustrate this, let me show you an "addressing circuit".

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faa844fd2-831e-4856-911b-b1b5659f2025_240x207.png "addressing cuicuit")

Here, A and B are the two-bit address lines, they represent the indices: 00, 01, 10, 11\. The output Z, Y, X and W are the selectors of the items in the array. Notice that an output selector is enabled only when both of the input lines of the corresponding AND gate is "1".

Now, ignore the input B and just look at A. See how its signal flows through the direct wires and the inverters. We can make the following observations:

*   When A is "1", then the AND gate of X and W will receive a "1" on one of their input ports, while the AND gate of Z and Y will receive a "0" on one of their input puts.

*   On the other hand, if A is "0", then the AND gate of X and W will receive a "0" on one of their input ports, while the AND gate of Z and Y will receive a "1" on one of their input puts.

<span>From the above, I hope you have seen that the value of A </span>_partially selects_<span> half of the AND gates -- it is either the set {X, W} or {Z, Y}. By "partially select", I mean they are not fully selected, because we haven't taken B into account. At this point, I hope you have noticed that A is in fact doing one step of a "binary search".</span>

Now we do a similar thing, but this time focus on B and ignore A. You should see a similar thing: depending on the value of B, either we partially select {Y, W}, or we partially select {Z, X}. So we can also think of B as doing one step of a "binary search".

Now, we see that A and B are each a step of a binary search, and it is interesting to see that B's selection will cut A's selection evenly, whether A is 0 or 1\. We can say the same thing vice versa: A's selection will cut B's selection evenly, whether A is 0 or 1.

Also notice that the selection of A and B can happen at the same time. That means, when they work simultaneously, it takes just O(1) for a binary search through an array of length 4. If we generalize this circuit to N bits of input, then within O(1) time, we can do a binary search through an array of length 2N.

This explains why indexing an array is faster than binary search, because it is a parallel binary search where (log n) steps happen at the same time.
