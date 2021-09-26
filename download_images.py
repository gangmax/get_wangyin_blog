#! /usr/bin/env python3
# Download the images used by WangYin's blog.
# Regular expression testing: https://regex101.com/
'''
不但测试数据的“普遍性”值得怀疑，AI 领域拿神经网络跟人比的时候，总喜欢用所谓“top-5 准确率”，也就是说给机器和人各自 5 次机会来给图片分类，看谁的准确率高。

![](https://www.yinwang.org/images/top-5-error.jpg)

![](http://www.yinwang.org/images/top-5-error.png)

[![](http://www.yinwang.org/images/caltrain-accident1.jpg)](http://www.ktvu.com/story/28193228/driver-killed-in-menlo-park-caltrain-accident-was-trapped-on-tracks)

你只需要上网搜一下，就基本有了线索：原来那些颗粒物是附近的工厂排出来的。工厂为了掩盖排烟的真相，都选择在晚上偷排，这样就不那么明显了。近一点的人可以看见，远一点的，混在夜幕中就看不见了。 ​ ![](http://www.yinwang.org/images/chengdu-air-cause1.jpg) ​ ![](http://www.yinwang.org/images/chengdu-air-cause2.jpg)

[![](http://www.yinwang.org/images/blackfish.jpg)](http://www.imdb.com/title/tt2545118) [![](http://www.yinwang.org/images/free-willy.jpg)](http://www.imdb.com/title/tt0106965)

具体一点，“top-5”是什么意思呢？也就是说对于一张图片，我可以给出 5 个可能的分类，只要其中一个对了就算我分类正确。比如图片上本来是汽车，我看到图片，说：

1.  “那是苹果？”
2.  “哦不对，是杯子？”
3.  “还是不对，那是马吧？”
4.  “还是不对，所以是手机？”
5.  “居然还是不对，那我最后猜它是汽车！”
'''

'''
2020-12-29: Update regex for the following missing image URL:

    (https://yinwang1.files.wordpress.com/2020/09/album_temp_1601205394.jpg?w=945&h=1552&zoom=2)

'''



import os
import re
import urllib.request

IMAGE_URL_PATTERNS = [
    '(\(http[s]{0,1}:\/\/www.yinwang.org\/images\/.+?g\))',
    '(\(http[s]{0,1}:\/\/yinwang1.files.wordpress.com\/\d+\/\d+\/[.A-Za-z0-9_-]+\.\w+g\?w=\d+&h=\d+\))',
    '(\(http[s]{0,1}:\/\/yinwang1.files.wordpress.com\/\d+\/\d+\/[.A-Za-z0-9_-]+\.\w+g\?w=\d+\))',
    '(\(http[s]{0,1}:\/\/yinwang1.files.wordpress.com\/\d+\/\d+\/[.A-Za-z0-9_-]+\.\w+g\))'
]

def get_imagelinks(blog_path):
    imagelinks = []
    # Filter files with extension: https://stackoverflow.com/a/3964696
    filenames = [f for f in sorted(os.listdir(blog_path)) if f.endswith('.markdown') or f.endswith('.md')]
    for fname in filenames:
        with open(blog_path + '/' + fname) as f:
            fcontent = f.readlines()
        for line in fcontent:
            for exp in IMAGE_URL_PATTERNS:
                matched = re.findall(exp, line)
                for x in matched:
                    imagelinks.append(x[1:-1])
    imagelinks.reverse()
    print(imagelinks)
    return imagelinks

def get_filename(url):
    file_name = url.split('/')[-1]
    if '?' in file_name:
        # Handle the situation like "album_temp_1601205394.jpg?w=945&h=1552&zoom=2".
        file_name = file_name.split('?')[0]
    return file_name

def download_image(url, image_path):
    urllib.request.urlretrieve(url, image_path + '/' + get_filename(url))

if __name__ == '__main__':
    blog_path = './blog'
    image_path = './image'
    imagelinks = get_imagelinks(blog_path)
    print('\nFind {} image links...\n'.format(len(imagelinks)))
    count = 0
    for url in imagelinks:
        print('Downloading {0}...'.format(url))
        download_image(url, image_path)
        count = count + 1
    print('Done({}).'.format(count))

