# -*- coding: utf-8 -*-




import os

import requests
from html2text import html2text

READABILITY_URL = 'https://www.readability.com/api/content/v1/parser'

def readability(url):
    token = os.environ.get('READABILITY_TOKEN')
    params = {'url': url, 'token': token}

    r = requests.get(READABILITY_URL, params=params)
    return r.json()['content']

def convert(html):
    return html2text(html)

def meh(url):
    try:
        return convert(readability(url))
    except KeyError:
        return None


if __name__ == '__main__':
    print meh('http://kennethreitz.org/')