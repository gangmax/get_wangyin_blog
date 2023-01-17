今天的第二个科普任务，推荐大家看看这个讲述 GPS 定位系统原理的视频：

<div id="youtube2-FU_pY2sTwTA" class="youtube-wrap" data-attrs="{&quot;videoId&quot;:&quot;FU_pY2sTwTA&quot;,&quot;startTime&quot;:null,&quot;endTime&quot;:null}">

<div class="youtube-inner"><iframe src="https://www.youtube-nocookie.com/embed/FU_pY2sTwTA?rel=0&amp;autoplay=0&amp;showinfo=0&amp;enablejsapi=0" frameborder="0" loading="lazy" gesture="media" allow="autoplay; fullscreen" allowautoplay="true" allowfullscreen="true" width="728" height="409"></iframe></div>

</div>

但他的图片有点问题，我改了一下。

原理其实比较简单，只需要基本的立体几何知识就能理解。可以用一句话概括为：“四个球面的交集只有一点。”现在我具体分析一下这句话是怎么应用的：

1.  GPS 卫星（或基站）发射的信息，里面带有发出时的「坐标」和「时间戳」。（图 1）

    <div class="captioned-image-container">

    <figure> [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97b3c58-0e82-4f87-8a75-30f5266b9114_1642x1046.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97b3c58-0e82-4f87-8a75-30f5266b9114_1642x1046.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97b3c58-0e82-4f87-8a75-30f5266b9114_1642x1046.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97b3c58-0e82-4f87-8a75-30f5266b9114_1642x1046.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97b3c58-0e82-4f87-8a75-30f5266b9114_1642x1046.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97b3c58-0e82-4f87-8a75-30f5266b9114_1642x1046.jpeg) </figure>

    </div>

2.  GPS 接收器收到这个信息，就能从「时间戳」算出这个 GPS 卫星到自己的距离 r1。r1 = 光速 * 传输时间。

3.  与这个卫星距离为 r1 的位置，全都处于一个半径为 r1 的球面上，为了方便我把它叫做“等距球”。几何学告诉我们，两个球面的交集是一个圆，所以这个“等距球”和地球的交集是一个圆（图 2a，需要一点 3D 想象能力）。看来只靠一个卫星的信号，我们没法知道自己具体的位置，只知道在一个圆上。

    <div class="captioned-image-container">

    <figure> [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6332f8f2-1335-4131-8ce3-9fbac7f8104a_582x467.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6332f8f2-1335-4131-8ce3-9fbac7f8104a_582x467.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6332f8f2-1335-4131-8ce3-9fbac7f8104a_582x467.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6332f8f2-1335-4131-8ce3-9fbac7f8104a_582x467.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6332f8f2-1335-4131-8ce3-9fbac7f8104a_582x467.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6332f8f2-1335-4131-8ce3-9fbac7f8104a_582x467.jpeg) </figure>

    </div>

4.  如果能收到第 2 个卫星的位置和距离，我们就能画出另一个球。两个卫星的“等距球”和地球，这三个球的交集就是我们可能处于的位置。这个交集大概率只有两点，但是我们不知道是哪一点。（图 2b）

    <div class="captioned-image-container">

    <figure> [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F361ac449-bb8c-441f-9aec-f5abb29fc551_776x591.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F361ac449-bb8c-441f-9aec-f5abb29fc551_776x591.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F361ac449-bb8c-441f-9aec-f5abb29fc551_776x591.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F361ac449-bb8c-441f-9aec-f5abb29fc551_776x591.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F361ac449-bb8c-441f-9aec-f5abb29fc551_776x591.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F361ac449-bb8c-441f-9aec-f5abb29fc551_776x591.jpeg) </figure>

    </div>

5.  如果能收到第 3 个卫星的位置和距离，它的“等距球”大概率会经过这两点中的其中一点，而不经过另一点。于是接收器在地面的坐标就确定了。（图 2c）

    <div class="captioned-image-container">

    <figure> [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F379714b3-fcca-43d9-8ba4-a437894468a1_768x807.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F379714b3-fcca-43d9-8ba4-a437894468a1_768x807.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F379714b3-fcca-43d9-8ba4-a437894468a1_768x807.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F379714b3-fcca-43d9-8ba4-a437894468a1_768x807.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F379714b3-fcca-43d9-8ba4-a437894468a1_768x807.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F379714b3-fcca-43d9-8ba4-a437894468a1_768x807.jpeg) </figure>

    </div>

6.  如果能收到第 4 个卫星的信号，那么它的“等距球”也会通过这一点，所以如果只需要地面坐标的话，并不需要第 4 个卫星。（图 2d）

    <div class="captioned-image-container">

    <figure> [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f861c4-2cbb-4b4a-80e2-1e41becd8954_776x816.jpeg 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f861c4-2cbb-4b4a-80e2-1e41becd8954_776x816.jpeg 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f861c4-2cbb-4b4a-80e2-1e41becd8954_776x816.jpeg 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f861c4-2cbb-4b4a-80e2-1e41becd8954_776x816.jpeg 1456w" sizes="100vw">![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f861c4-2cbb-4b4a-80e2-1e41becd8954_776x816.jpeg)</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f861c4-2cbb-4b4a-80e2-1e41becd8954_776x816.jpeg) </figure>

    </div>

<span>说了这么多，其实可以用一句话来理解它的原理：</span>**四个球面的交集只有一点**<span>。三个卫星的“等距球”加上地球，一共四个球，所以它们的交集是唯一的，只有一点。</span>

注意，这里的信号不一定需要从卫星发出来。地面基站上标记了坐标的，也能发射同样的信号（坐标+时间戳），接收器就能同样的方式算出自己的位置，就是简单的几何交集计算。

练习 1：第 2 个步骤里面，因为接收器的时钟和 GPS 卫星的时钟之间一般会有差距，所以只收到一个信息是不能得到「传输时间」的。但同一个卫星发出两个信息，就能消去这个差距，算出传输时间来。可以自己想想这是为什么？

练习 2a：第 4 个步骤里，我说两个卫星的等距球和地球的交集，“大概率”只有两个点。在什么特殊情况下，这个交集不只是两个点呢？它可能是什么其它形状？

练习 2b：第 5 个步骤里，我说第 3 个卫星的等距球“大概率”会经过其中一点，而不经过另一点。在什么特殊情况下，它的等距球会同时经过这两点呢？

练习 3：如果有 4 颗卫星的信号，那么不但能算出坐标，而且能算出海拔高度，所以第 4 颗卫星还是有用的。想想这是为什么？

练习 4：如果完全依靠地面的基站，我们能用三个基站的信号算出坐标。如果有第四个基站的信号，我们能算出海拔高度吗？如果能算出海拔高度的话，需要这四个基站的位置满足什么条件？

练习 5：如果练习 4 的设想可行的话，请你设计一个“地面 GPS 系统”，它不需要使用卫星，却能完全实现 GPS 卫星系统的功能，能满足日常的车辆行人导航，航空，航海，登山，越野等活动的需求。系统需要经济实惠，不超过基于卫星的系统的开销。
