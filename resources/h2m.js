#!/usr/bin/env node

/*
 * Before using this script, you need to install "nodejs" first, and then
 * the "to-markdown" and "request" npm packages as well. At this moment I'm
 * using:
 *
 * node.js: 6.0.0
 * to-markdown: 3.0.0
 * request: 2.72.0
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
 * Created by Max Huang.
 */

const request = require('request');
const toMarkdown = require('to-markdown');

// 1. Get the parameters.
var url = process.argv[2];
var startToken = process.argv[3];
var endToken = process.argv[4];

// 2. Read the HTML file content.
request(
  {uri: url, gzip: true},
  function(error, response, body){
    if(!error) {
      var fromIndex = body.indexOf(startToken);
      var toIndex = body.indexOf(endToken);
      if (fromIndex >= 0 && fromIndex < toIndex) {
        // 2. Convert the HTML content to markdown format.
        var content = body.substring(fromIndex + startToken.length, toIndex);
        // console.log(content);
        var md = toMarkdown(content.toString());
        // 3. Write the markdown content.
        // console.log("This is the MD content:");
        console.log(md);
      }
    } else {
      console.error(error);
    }
  });
