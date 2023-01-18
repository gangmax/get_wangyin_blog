# On linux kernel memory addressing

From [here](https://yinwang0.substack.com/p/linux-mem).

<span>I got addicted to this book named</span> _Understanding the Linux Kernel_ <span>by Daniel Bovet and Marco Cesati, which I happened to have picked up from a shelf. I wrote Linux drivers when I was an undergrad and (unfortunately) had to read quite some Linux kernel code in order to figure things out. How time flies. I finally got my breath back and have some time to read more of it. This time I look at the Linux kernel in a very different perspective, as you will see.</span>

Today I just finished reading the second chapter "Memory Addressing" which talks about two different ways of addressing memory: segmentation and paging, and also some details into memory management. I'm going to make some observations that interested me.

##### The essential difference between segmentation and paging

<span>Segmentation and paging are similar in the sense that they both provide some kind of</span> _indirection_ <span>or</span> _mapping_ <span>from one address to another:</span>

*   Segmentation maps an "offset address" to a "linear address".

*   Paging maps a "virtual address" to a "physical address".

Those are what every textbook tells us, but if you ponder a while on them, you will find that they don't make much sense. You know these fancy names and facts about them, and that most people tell you to use paging, not segmentation, so what? What the heck is the difference between segmentation and paging, and why should segmentation be inferior? If you have the same feeling as I do, this is the section that you may want to read and write comments for.

_**Segmentation and its historical purpose**_

On the surface, segmentation maps an "offset address" to a "linear address". From a history perspective, segmentation had been mainly designed as a workaround for limited register size in early processors. Because early processors (especially the x86 family) have more memory address pins than their data paths, they can't use the registers alone to address all available memory. They had to logically subdivide the memory into segments, and use segment descriptors to extend the registers' address range. This idea can be captured in this simple formula:

length(SegmentBase) + length(Offset) = length(LinearAddress)

The segments' base addresses are usually stored somewhere in the main memory, so they have virtually unlimited size, which compensates the limitations of register addressing.

Of course this mechanism is tedious and inconvenient to use, but it served its purpose in the early days. Unfortunately even in the modern age where data paths are of good size (64-bit), some processors have this mechanism built-in and force the OS writers to use segmentation. In fact, Linux sets all the segment base addresses to zero and limits to all the address space, so it essentially bypassed the use of segmentation.

_**Paging and its connection to "automatic memory management"**_

Paging maps a "virtual address" to a "physical address". The size of a virtual address has no set relation with the size of a physical address, so no formula about the sizes can be provided.

<span>Paging has an interesting connection with "automatic memory management" in high-level languages such as Java (or Scheme, Python, Ruby, ...). Basically, mapping a new page in the page table is equivalent to object creation in Java. If you look at this carefully, the Unix systems allocate memory to a process in the size of</span> _pages_<span>, instead of</span> _objects_<span>, and the process then use virtual addresses to further subdivide the chuck of memory that is allocated to it.</span>

An intuition can be seen from the following side-by-side comparison (in a mythical machine where a page has only five bytes).

Java:     String s = new String("hello"); kernel:  map page frame 0x00000000--0x00000004 to physical page 0x00200cf2--0x00200cf6.

<span>Here the physical page 0x00200cf2--0x00200cf6 corresponds to the storage for the new String object, while the page frame 0x00000000--0x00000004 corresponds to the</span> _object name_ <span>s. The hardware mapping corresponds to variable binding in the Java language. This analogy might require some twist of mind, but I think it pretty much captures the essence of paging.</span>

_**Segmentation is just paging, with a fixed number of pages**_

Despite of the history of segmentation, we can't eliminate it from our choice for a memory management mechanism just by prejudice. Really, paging has won for a reason. We can see it from the observations I just made.

From the analogy I made from paging to "automatic memory management", we can see that the virtual addresses are actually "holders" for the allocated memory blocks, similar to variable names in Java. Linux programs access the allocated memory by using addresses (and may further subdivide the allocated memory blocks, e.g., using "malloc" in the standard C library). This allocation can be readily extended to additional memory blocks in arbitrary locations. We just need to find free physical pages and make mappings in the page tables. The programs then access the addition pages using the addresses that have already been there.

<span>But this is not the case with segmentation. Yes, the segments provide some kind of abstraction, but we can basically view each segment as one page (with a flexible size though). How many such "pages" can a program have for its data? Just count the number of segment registers (cs, ds, es, ss, ... ). In fact, you can't really concatenate those "pages" and use them all together, because</span> _they must be accessed by their names_<span>. So in effect a program usually has only one "page" for its dynamic data.</span>

A huge problem comes when we need to extend the allocation. Once allocated to a program, the segment will have fixed base and limit. Imagine how we could extend the allocation if the original space becomes too small after some use? We would have to find a larger block of memory (in another address if the limit can't be extended any further), copy the data to the newly found block, change the segment descriptor, reload the segment selection registers. This is doomed to inefficiency of course.

<span>Just think about it carefully, you will find some truth in this sentence:</span> _Segmentation is just paging, but with a fixed (and very small) number of pages_<span>.</span>

**Question 1.1**

For a deeper understanding about paging, think about swapping. Swapping happens when there is not enough physical memory for new allocations. In that case, the following things happen:

1.  The kernel has to store some pages on disk and load them back into memory later.

2.  <span>When a page is swapped back, it could occupy a</span> _different_ <span>physical page.</span>

3.  <span>The program's page table has to be</span> _updated_ <span>to map the corresponding process page frame to the physical page where the page is loaded into.</span>

Here comes the question: What is an analogy of this phenomenon in a high-level language program (demonstrating all the three phenomena above)?

**Questions 1.2**

What property of segmentation prevents us from making a similar analogy---from segmentation to automatic memory management in high-level languages?
