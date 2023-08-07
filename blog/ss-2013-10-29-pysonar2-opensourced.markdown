# PySonar2 opensourced

From [here](https://yinwang1.substack.com/p/pysonar2).

<span>As mentioned in a</span> [post](http://yinwang0.wordpress.com/2010/09/12/pysonar) <span>several years ago, I made an advanced Python static analyzer at Google. It turns out that this piece of code is still the most advanced static analysis for Python until today. But because of one highly tricky bug inside the analyzer, it had serious performance issues.</span>

Only recently I revived my interest in it and fixed the bug by commenting out two lines of code ;-) After mutual agreement with Google, I can now release PySonar's second version code (call it PySonar2). The code is now open for downloading on my GitHub repo:

> [https://github.com/yinwang0/pysonar2](https://github.com/yinwang0/pysonar2)

The build process is not friendly at the moment, but please bear with me to fix it.

I have been working on it sporadically in the past few days, fixed several bugs. It can now produce good results for Python 2.5, 2.6, 2.7 standard libraries and projects like Django framework, with pretty good performance (should finish said projects in several minutes on a laptop).

Although PySonar2 contains some of the world's most advanced static analysis techniques, Python is a very complex language to analyze, so corner case bugs are almost unavoidable. Please file an issue on GitHub if you find one. I'll try to fix it when I get time.
