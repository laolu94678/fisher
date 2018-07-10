#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @File    : helpers.py.py
    @Time    : 2018/7/10 下午7:09
    @Author  : 老卢
    @desc    : 验证性函数等
'''

# 该方法判断关键字与ISBN码
def is_isbn_or_key(word):
    '''
    :q: 关键字及 ISBN码
    :return: page 图书列表

    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key