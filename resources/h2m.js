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
 * Usage: ./h2m.js http://www.yinwang.org/blog-cn/2014/04/18/golang/index.html
 *
 * Created by Max Huang.
 */

var request = require('request');
var toMarkdown = require('to-markdown');
// 1. Read the HTML file content.
request(
  {uri: process.argv[2], gzip: true},
  function(error, response, body){
    if(!error) {
      var fromIndex = body.indexOf('<body>');
      var toIndex = body.indexOf('</body>');
      if (fromIndex >= 0 && fromIndex < toIndex) {
        // 2. Convert the HTML content to markdown format.
        var content = body.substring(fromIndex + '<body>'.length, toIndex);
        console.log(content);
        var md = toMarkdown(content.toString());
        // 3. Write the markdown content.
        console.log(md);
      }
    } else {
      console.error(error);
    }
  });
