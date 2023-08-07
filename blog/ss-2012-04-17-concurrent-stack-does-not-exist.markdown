# Concurrent stack does not exist

From [here](https://yinwang1.substack.com/p/concurrent-stack).

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb92d92c2-efc5-4d1f-9823-05123f0b46bc_150x230.jpeg)

<span>Some weeks ago I read this thought-provoking article by Nir Shavit</span> _[Data Structures in the Multicore Age](http://cacm.acm.org/magazines/2011/3/105308-data-structures-in-the-multicore-age)_<span>. The topic is about efficiency of concurrent data structures. There have been many thinkings going on after the reading, but the most interesting point to me is that the author started trying to use a "concurrent stack", but ended up happily using a pool.</span>

> "In the end, we gave up the stack's LIFO ordering in the name of performance."

Now there can be several interesting questions to ask. Can we give up some property of a data structure if it is crucial to the correctness of the program? If we can give up the LIFO ordering, then why did we think we need a stack? But the most interesting question is probably:

> Does a "concurrent stack" really exist?

I think the answer is No -- a "concurrent stack" hasn't ever existed. Here is why:

1.  If the threads are allowed to push and pop concurrently, then the "stack" can't really maintain a LIFO order, because the order of the "ins" and "outs" is then indeterminate and contingent on the relative execution speeds of the threads.

2.  If the execution of two threads strictly interleave. Each time a "pusher" pushes an element, a "popper" immediately pops it out, then this is a FIFO order, a queue.

3.  <span>If a pusher pushes</span> _all_ <span>the elements before a popper starts to pop</span> _all_ <span>of them out, then this is indeed a LIFO order, a stack. But notice that there is no concurrency in this case -- the executions of the threads must be completely sequential, one after another.</span>

4.  If two threads interleave randomly, or there are more than two threads accessing the "stack" at the same time, then nothing can be said about the access order.

From the above, we can see that there is a fundamental conflict between the two notions, "concurrency" and a "stack".

> If a "stack" can be accessed concurrently, then there is no way we can maintain a LIFO order. On the other hand, if we enforce a LIFO order, then the stack cannot be accessed concurrently.

If we have realized that the essence of a stack is a continuation, and a continuation (by itself) is sequential, then it is no surprise we arrive at this conclusion.

Since a LIFO order is essential to a stack, we can't call the data structure a "stack" if we can't maintain a LIFO order.

> We can't call a data structure a "stack" just because it has the methods named "push" and "pop" -- we have to look at what the methods actually do.

<span>Even if we continue to think that we are using a stack, the threads are in effect just</span> _distributing_ <span>messages, with the operations "push = send" and "pop = receive". So in essence this data structure is a</span> _pool_<span>. This exactly justifies the author's relaxation to a pool, although no actual relaxation happens -- the data structure has been a pool from the beginning. It was just disguised as a stack and less efficient.</span>

So we see that the concept of a "concurrent stack" does not really exist. We also see that some data structures we have in the sequential world may not have concurrent counterparts.
