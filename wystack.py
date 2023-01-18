#!/usr/bin/env python

# This script is used to do download the blog items of Wangyin's substack
# websites below and convert them into the markdown format:
#
#   https://yinwang0.substack.com/
#   https://yinwang1.substack.com/
#
# To run this scirpt, first please make sure you have all the dependencies
# in the "requirements.txt" file installed, and the execute:
#
#   ./wystack.py

import json
import os
import re
import sys
import requests
from slugify import slugify

PAGE_SIZE = 12
INDEX_URL = (
    'https://yinwang1.substack.com/api/v1/archive?sort=new&limit={}&offset={}'
)
PAGE_CONTENT_START_TAG = '<div dir="auto" class="body markup">'
PAGE_CONTENT_END_TAG = '<div class="post-footer use-separators">'
BASE_BLOG_PATH = "./blog"
FILTERED_LINES_PATTERNS = [
    '^\<div class=\"captioned-image-container\"\>$',
    '^\<div\>$',
    '^\</div\>$',
    '^\<figure\>$',
    '^\</figure\>$',
    '^\<div id=\"youtube2-.+\"\>$',
]
MATCHED_PATTERNS = {
    '.*\<div class=\"image2-inset\"\>.+\!\[.*\]\((.+)\)\<\/picture\>': '![]({})',
    '^\<div class=\"youtube-inner\">\<iframe src=\"(.+)\?.+\<\/div\>$': '[Video]({})',
}


def parse_index(index_url):
    '''
    Return a list of post items, each item contains the post basic info.
    '''
    response = requests.get(index_url)
    items = json.loads(response.text)
    result = []
    for item in items:
        pid = item['id']
        title = item['title']
        url = item['canonical_url']
        date = item['post_date'][0:-14]
        result.append({'id': pid, 'title': title, 'url': url, 'date': date})
    return result


def get_filename(item):
    return 'ss-{}-{}.markdown'.format(item['date'], slugify(item['title']))


def parse_page_to_post(
    page_url, start_tag=PAGE_CONTENT_START_TAG, end_tag=PAGE_CONTENT_END_TAG
):
    '''
    Return a string which contains the post content in markdown format.
    '''
    stream = os.popen(
        "./resources/h2m.js '{}' '{}' '{}'".format(page_url, start_tag, end_tag)
    )
    return stream.read()


def is_filtered_line(line: str) -> bool:
    for item in FILTERED_LINES_PATTERNS:
        m = re.fullmatch(item, line)
        if m is not None:
            return True
    return False


def optimize_content(raw: str, title: str, url: str) -> str:
    '''
    Optimize the text content by:
        1. Remove the useless html tags such as "<div>" and "</div>".
        2. Convert the original image tag to readable content.
    '''
    result = '# {}\n\nFrom [here]({}).\n\n'.format(title, url)
    last_line = ''
    for line in raw.splitlines():
        if len(line) == 0 or is_filtered_line(line):
            line = ''
        else:
            for pattern in MATCHED_PATTERNS.keys():
                m = re.search(pattern, line)
                if m is not None:
                    line = MATCHED_PATTERNS[pattern].format(m.group(1))
        if last_line == '' and line == '':
            result = result
        else:
            result = result + line + '\n'
        last_line = line
    return result


def write_post(content, target_filename, target_dir):
    with open('{}/{}'.format(target_dir, target_filename), 'w') as f:
        f.write(content)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        from_batch_num = 0
        to_batch_num = int(sys.argv[1])
    elif len(sys.argv) == 3:
        from_batch_num = int(sys.argv[1])
        to_batch_num = int(sys.argv[2])
    else:
        from_batch_num = 0
        to_batch_num = 1
    for i in range(from_batch_num, to_batch_num):
        given_url = INDEX_URL.format(PAGE_SIZE, PAGE_SIZE * i)
        items = parse_index(given_url)
        print('Find total "{}" posts on "{}"...'.format(len(items), given_url))
        for item in items:
            target_dir = BASE_BLOG_PATH
            filename = get_filename(item)
            print('Fetching the "{}/{}" post...'.format(target_dir, filename))
            raw_content = parse_page_to_post(item['url'])
            result_content = optimize_content(
                raw_content, item['title'], item['url']
            )
            write_post(result_content, filename, target_dir)
    print('Done.')
