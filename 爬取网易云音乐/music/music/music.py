#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import requests

def get_html(url):
    return requests.get(url).content
html=get_html("https://www.baidu.com")
print(html)
