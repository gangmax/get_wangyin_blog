# 航海与GPS

From [here](https://yinwang1.substack.com/p/gps-c90).

<span>了解到一些关于航海导航的信息。航海的时候 GPS 系统也是靠不住的，都在用「</span>[Differential GPS](https://en.wikipedia.org/wiki/Differential_GPS)<span>」，一种基于地面基站的系统，使用长波从港口往海里发射信号。</span>

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9db9a0c-34c0-44c1-8508-c7e1611190b5_1935x1417.jpeg)

天上不是有“GPS 卫星”吗？为什么还得依靠地面的系统？虽然表面上说是“对卫星 GPS 系统的增强”，然而解读一下，就会发现“卫星 GPS”在海里其实是不能用的，或者根本就是不存在的。

如果你理解了我之前分析的 GPS 工作原理，就会发现地面基站只需要标记自己的坐标就能独立进行定位。标注地面坐标是一劳永逸，不会变的，然后不停地广播自己的位置和时间戳就可以了，不需要再依赖其它信号。那还有什么必要去“增强卫星信号”呢？

可能有人会说，从海边广播太远了，需要很大的功率。然而你知道“GPS 卫星”离地面的距离是多少吗？去查一下吧，然后再看看地球的周长是多少，太平洋的宽度是多少。比较一下，看看是谁需要更大的功率？
