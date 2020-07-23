# get_wangyin_blog

A Clojure program to download [WangYin's blog](http://www.yinwang.org/) articles and convert them into the [markdown](https://en.wikipedia.org/wiki/Markdown) format.

Before running please make sure you have "Java/Leiningen/node.js" installed. The versions I'm using are:

```
java: 11.0.7-open
leiningen: 2.9.4
node.js: v12.18.3
```

The "node.js" part of this project is used to convert the HTML page content into markdown format text. Before running, install the npm packages first:

```bash
npm install
```

Now you're good to go:

## Usage

```bash
lein run
```

## License

Copyright © 2014 Max Huang

Distributed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt).
