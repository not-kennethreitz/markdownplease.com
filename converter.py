# -*- coding: utf-8 -*-

import os

from mercury_parser import ParserAPI
from html2text import html2text

mercury = ParserAPI(api_key=os.environ['MERCURY_API_KEY'])

def convert(html, title=None):
    if title:
        title = '# {}'.format(title)
        html = '\n\n'.join([title, html])

    return html2text(html)

def meh(url):
    try:
        d = mercury.parse(url)
        return convert(d.content, title=d.title)
    except KeyError:
        return None


if __name__ == '__main__':
    print meh('http://kennethreitz.org/')