# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, Markup
from converter import get_readable_content_from_url
from markdown import markdown


app = Flask(__name__)


def _markdown_to_html(text):
    return Markup(markdown(text))


@app.route('/')
def fuck_gpl3():
    url = request.args.get('url')
    type = request.args.get('type', 'markdown')

    content = get_readable_content_from_url(url)
    print url

    if url:
        if not content:
            return '404 Not Found', 404

        if type == 'html':
            print url
            markdown_url_contents = _markdown_to_html(content)
            return render_template(
                'index.html',
                converted_url_contents=markdown_url_contents,
                page_url=url,
            )
        else:
            return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
