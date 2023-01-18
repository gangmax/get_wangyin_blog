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
from functools import partial
from slugify import slugify

INDEX_URL = 'https://yinwang1.substack.com/api/v1/archive?sort=new&limit=12&offset=0'
PAGE_CONTENT_START_TAG = '<div dir="auto" class="body markup">'
PAGE_CONTENT_END_TAG = '<div class="post-footer use-separators">'
BASE_BLOG_PATH = "./blog"
FILTERED_LINES_PATTERNS = [
    '^\<div class=\"captioned-image-container\"\>$',
    '^\<div\>$',
    '^\</div\>$',
    '^\<figure\>$',
    '^\</figure\>$',
    '',
]

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
        result.append({
            'id': pid,
            'title': title,
            'url': url,
            'date': date})
    return result

def get_filename(item):
    return 'ss-{}-{}.markdown'.format(item['date'], slugify(item['title']))

def parse_page_to_post(page_url, start_tag = PAGE_CONTENT_START_TAG,
    end_tag = PAGE_CONTENT_END_TAG):
    '''
    Return a string which contains the post content in markdown format.
    '''
    stream = os.popen("./resources/h2m.js '{}' '{}' '{}'".format(
        page_url, start_tag, end_tag))
    return stream.read()

def convert_image_tag(content: str) -> str:
    m = re.search(r'\!\[.*\]\((.+)\)\<\/picture\>', content)
    return '![]({})'.format(m.group(1))

def is_filtered_line(line: str) -> bool:
    for item in FILTERED_LINES_PATTERNS:
        m = re.fullmatch(item, line)
        if m is not None:
            return True
    return False

CONVERTING_FUNCTION_MAP = {
    '[<div clas': convert_image_tag,
    '<figure> [': convert_image_tag,
}

def optimize_content(raw: str, title: str, url: str) -> str:
    '''
    Optimize the text content by:
        1. Remove the useless html tags such as "<div>" and "</div>".
        2. Convert the original image tag to readable content.
    '''
    result = '#{}\n\nFrom [here]({}).\n\n'.format(title, url)
    last_line = ''
    for line in raw.splitlines():
        if len(line) == 0 or is_filtered_line(line):
            line = ''
        elif line[0:10] in CONVERTING_FUNCTION_MAP.keys():
            converted = CONVERTING_FUNCTION_MAP[line[0:10]](line)
            if len(converted) > 0:
                line = converted
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
    given_url = sys.argv[1] if len(sys.argv) > 1 else INDEX_URL
    items = parse_index(given_url)
    print('Find total "{}" posts...'.format(len(items)))
    for item in items:
        target_dir = BASE_BLOG_PATH
        filename = get_filename(item)
        raw_content = parse_page_to_post(item['url'])
        result_content = optimize_content(raw_content, item['title'], item['url'])
        write_post(result_content, filename, target_dir)
        print('Finish getting the "{}/{}" post...'.format(target_dir, filename))
    print('Done.')
