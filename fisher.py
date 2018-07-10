#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : fisher.py
@Time    : 2018/7/9 上午11:25
@Author  : 老卢
 @desc    : 主文件
'''

from flask import Flask
from helpers import is_isbn_or_key

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/book/search/<q>/<page>')
def search(q,page):
    # 判断关键字与ISBN码
    isbn_or_key = is_isbn_or_key(q)
    return isbn_or_key

if __name__ == '__main__':
    app.run()