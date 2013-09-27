# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template
from converter import meh

app = Flask(__name__)

@app.route('/')
def fuck_gpl2():
    url = request.args.get('url')

    if url:
        content = meh(url)
        if content:
            return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
        else:
            return '404 Not Found', 404
    else:
        return render_template('index.html')
