# -*- coding: utf-8 -*-

import os

import requests
from html2text import html2text

_READABILITY_URL = 'https://www.readability.com/api/content/v1/parser'

def _readability(url):
    token = os.environ.get('READABILITY_TOKEN')
    params = {'url': url, 'token': token}

    r = requests.get(_READABILITY_URL, params=params)
    decoded_content = (
        r.json()['content'],
        r.json()['title'],
    )
    return decoded_content

def _convert(html, title=None):
    if title:
        title = '# {}'.format(title)
        html = '\n\n'.join([title, html])

    text_from_html = html2text(html)
    return text_from_html

def get_readable_content_from_url(url):
    try:
        content, title = _readability(url)
        return _convert(content, title=title)
    except KeyError:
        return None


if __name__ == '__main__':
    print get_readable_content_from_url('http://kennethreitz.org/')
