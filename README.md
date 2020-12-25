This project contains some programs that download WangYin's blogging posts from his websites [here](http://www.yinwang.org/) and [here](https://yinwang1.wordpress.com/),  and convert them into text files in the [markdown](https://en.wikipedia.org/wiki/Markdown) format.

Distributed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt).

---

## The Clojure part for "http://www.yinwang.org/"

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


```bash
lein run
```

---

## The Python part for "https://yinwang1.wordpress.com/"

Setup the "node.js" environment as above, and make sure you have Python3 installed. Install the Python libraries first:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
./wywp.py
```

