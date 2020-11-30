#!/usr/bin/env node

/*
 * Before using this script, you need to install "nodejs" first, and then
 * the "to-markdown" and "request" npm packages as well. At this moment I'm
 * using:
 *
 * node.js: 6.0.0
 * to-markdown: 3.1.1
 * got: 11.5.1
 *
 * This script is used to convert an HTML file into a markdown format string
 * which is based on:
 *
 *   https://github.com/domchristie/to-markdown/
 *
 * Usage 1(WangYin's blog):
 *   ./h2m.js 'http://www.yinwang.org/blog-cn/2020/06/10/new-ugly-chinese' '<div class="inner">' '</body>'
 *
 * Usage 2(1bypte blog):
 *  ./h2m.js 'https://1byte.io/leancloud-story-avos/' '<article>' '</article>'
 *
 * Usage 3(Wangyin's WP):
 *  ./h2m.js 'https://yinwang1.wordpress.com/2020/09/13/chinese-characteristics-1/' '<div class="post-content clear">' '<div id="atatags-370373'
 *
 * Created by Max Huang.
 */

const toMarkdown = require('to-markdown');
const got = require('got');

// 1. Get the parameters.
var url = process.argv[2];
var startToken = process.argv[3];
var endToken = process.argv[4];

// 2. Read the HTML file content.
(async () => {
    try {
        const response = await got(url);
        let fromIndex = response.body.indexOf(startToken);
        let toIndex = response.body.indexOf(endToken);
        if (fromIndex >= 0 && fromIndex < toIndex) {
            // 2. Convert the HTML content to markdown format.
            let content = response.body.substring(fromIndex + startToken.length, toIndex);
            // console.log(content);
            let md = toMarkdown(content.toString());
            // 3. Write the markdown content.
            // console.log("This is the MD content:");
            console.log(md);
        } else {
            let md = toMarkdown(response.body.toString(0));
	    console.log(md);
	}
    } catch (error) {
        console.error(error);
    }
})();

