#!/usr/bin/env python

# This script is used to do download the blog items of Wangyin's WordPress
# website below and convert them into the markdown format:
#
# https://yinwang1.wordpress.com/
#
# To run this scirpt, first please make sure you have all the dependencies
# in the "requirements.txt" file installed, and the execute:
#
#   ./wywp.py

import json
import os
import re
import requests
from urllib.parse import quote, unquote

INDEX_URL = 'https://yinwang1.wordpress.com/?infinity=scrolling'
INDEX_POST_DATA = {
    'action': 'infinite_scroll',
    'page': '1',
    'order': 'DESC',
    'query_args[posts_per_page]': '1000',
}
INDEX_DATE_TITLE_REGEX = r'(\d{4})/(\d{2})/(\d{2})/(.*)/$'
PAGE_CONTENT_START_TAG = '<div class="post-content clear">'
PAGE_CONTENT_END_TAG = '<div id="atatags-370373'
PAGE_CONTENT_BACKUP_END_TAG = '<div id="jp-post-flair"'
BASE_BLOG_PATH = "./blog"

def parse_index(index_url = INDEX_URL, post_data = INDEX_POST_DATA,
    date_title_regex = INDEX_DATE_TITLE_REGEX):
    '''
    Return a list of post items, each item contains the post basic info.
    '''
    response = requests.post(index_url, data = post_data)
    raw_urls = json.loads(response.text)['postflair']
    result_urls = []
    for key in raw_urls.keys():
        pid = raw_urls[key]
        url = unquote(key)
        original_url = key
        pre = re.findall(date_title_regex, url)
        date = '{0}-{1}-{2}'.format(pre[0][0], pre[0][1], pre[0][2])
        title = pre[0][3]
        result_urls.append({
                'id': pid,
                'title': title,
                'url': url,
                'original_url': original_url,
                'date': date})
    return result_urls

def parse_page_to_post(page_url, start_tag = PAGE_CONTENT_START_TAG,
    end_tag = PAGE_CONTENT_END_TAG,
    backup_end_tag = PAGE_CONTENT_BACKUP_END_TAG):
    '''
    Return a string which contains the post content in markdown format.
    '''
    stream = os.popen("./resources/h2m.js '{}' '{}' '{}' '{}'".format(
        page_url, start_tag, end_tag, backup_end_tag))
    return stream.read()

def write_post(content, target_filename, target_dir):
    with open('{}/{}'.format(target_dir, target_filename), 'w') as f:
        f.write(content)

def get_filename(item):
    return 'wp-{}-{}.markdown'.format(item['date'], item['title'])

if __name__ == '__main__':
    items = parse_index()
    print('Find total "{}" posts...'.format(len(items)))
    for item in items:
        target_dir = BASE_BLOG_PATH
        filename = get_filename(item)
        content = parse_page_to_post(item['original_url'])
        write_post(content, filename, target_dir)
        print('Finish getting the "{}/{}" post...'.format(target_dir, filename))
    print('Done.')
