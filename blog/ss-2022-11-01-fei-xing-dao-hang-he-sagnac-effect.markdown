#飞行导航和 Sagnac effect

From [here](https://yinwang1.substack.com/p/sagnac-effect).

看了两个非常好的介绍飞机上的导航装置的视频：

1\. INS（Inertial Navigation System）

[Video](https://www.youtube-nocookie.com/embed/Pq_PDaYclAw)

2\. IRS（Inertial Reference System）

[Video](https://www.youtube-nocookie.com/embed/mUWlrlRcb0Q)

就像我之前说的，飞机导航是不依靠 GPS 的。使用 INS 或者 IRS，飞机完全不依靠外部信号就能确定自己在地球上的位置。INS 和 IRS 的原理一样，差别只是里面用的陀螺仪不一样。INS 用的是机械陀螺仪，而 IRS 用的是激光陀螺仪。

很有意思的是 IRS 的激光陀螺仪（ring laser gyroscope），依靠的是一个环状光路的装置。由于机身的旋转，两束激光到达终点的时间会不一样。

如下图所示，如果机身没有旋转，那么两束光会同时到达终点。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F031ab636-d195-442d-b608-b9777eda6ed8_1318x1318.jpeg)

但如果机身向右旋转了，那么左边的光会比右边的更晚到达终点。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe80f9601-e12c-42ce-99ad-f9a233a555fd_1327x1327.jpeg)

<span>依靠这个原理，IRS 可以探测到非常细微的旋转，随时更新机身的方向。这个现象叫做</span> [Sagnac effect](https://en.wikipedia.org/wiki/Sagnac_effect)<span>，是法国物理学家 Georges Sagnac 发现的。有意思的是，他当年设计这个实验是为了证明以太的存在。</span>

我不知道以太是否存在，但我觉得 Sagnac effect 确实证明了绝对参考系的存在，而且证明了相对论是错误的。好些其它科学家也这么认为，但主流科学界却否认这个说法。Wikipedia 上面说 Sagnac effect 是和狭义相对论一致的，原因是 Sagnac effect 需要旋转，所以不是惯性系，不符合相对论的前提条件。

但我感觉这是在诡辩，硬要套用“惯性系”这个前提，而没有看到相对论并不依赖于惯性系。相对论的真正前提是“相对光速不变”，但如果相对光速不变的话，激光陀螺仪是不可能正确工作的。激光陀螺仪能够成功用于精确的飞行导航，也说明了“绝对参考系”的存在。它说明存在一个“静止空间”，这样 IRS 才可能进行不依赖于任何外部信号的导航。也许相对于整个宇宙这个空间并不是静止的，但它至少是不随地球一起转动的。

一百多年了，相对论除了发展出一大堆空洞玄乎的理论，对世界到底有什么实际的贡献，每个人却都膜拜爱因斯坦，把他叫做天才。Sagnac effect 每天都对世界起着至关重要的作用，却没人知道它是怎么回事。爱因斯坦吐舌头的照片一大堆，Wikipedia 上面甚至都没有一张 Georges Sagnac 的照片。
