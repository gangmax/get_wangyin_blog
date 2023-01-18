#PySonar2 successfully integrated with Sourcegraph.com

From [here](https://yinwang1.substack.com/p/pysonar-sourcegraph).

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffee5e0a7-77b4-4781-8d1e-c49aa330eb6f_400x162.png)

<span>(The above picture was taken from: </span>[http://sourcegraph.com/github.com/mitsuhiko/flask](http://sourcegraph.com/github.com/mitsuhiko/flask)<span>) I recently joined a newly founded company called</span> [Sourcegraph.com](http://www.sourcegraph.com)<span>. We build an intelligent code search engine using some of the most powerful programming language technologies. The difference between Sourcegraph and other code search sites is: Sourcegraph truly understands code and produces accurate results. Sourcegraph lets you</span> _semantically_ <span>search and browse opensource code on the web in a similar fashion as you do locally with IDEs. It also finds users of your code worldwide, and show exactly how they use your code. For example the following is what Sourcegraph shows you about</span> [Flask](http://sourcegraph.com/github.com/mitsuhiko/flask)<span> framework's Flask.route method.</span>

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fda33ecc0-1142-4f25-9785-07fb537aa86b_300x279.png "code examples of Flask.route")

### PySonar2 integration

<span>Two weeks since joining, I have successfully integrated</span> [PySonar2](http://github.com/yinwang0/pysonar2)<span>'s type inference and indexing features with Sourcegraph.com, so that it can now show inferred types for Python functions. This is an advanced feature currently not available in any Python IDE. For example, the following is the "Top Functions" page for the</span> [Flask framework](http://flask.pocoo.org)<span>, showing the PySonar2 inferred types. Notice that the parameters are not type-annotated. PySonar2 infers the types by an advanced interprocedural analysis.</span>

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0dc15852-72b5-4cb2-8dba-e48c37f6bf33_300x240.png)

### How to use sourcegraph.com to browse your GitHub repo

<span>You can browse your GitHub by prepending "</span>`http://sourcegraph.com/`<span>" to your GitHub repo's address. For example, if your repo address is github.com/myname/myrepo, then you put this address into the browser:</span>

> http://sourcegraph.com/github.com/myname/myrepo

Currently this trick works only for GitHub addresses. If Sourcegraph hasn't yet processed the repo, it will queue it and start analyzing as soon as possible. Usually this finishes within a few minutes up to half an hour, depending on how large the repository is and how busy the servers are. Sourcegraph currently supports Go, JavaScript, Python and Ruby. More languages are under development. All our features are still in beta and may contain quite some bugs and many areas of improvements. You are very welcome to send bug reports and feature requests to us.
