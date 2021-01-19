#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/kantan-tools/下载页面内容/main.py
# @DATE: 2021/01/19 Tue
# @TIME: 17:19:48
#
# @DESCRIPTION: 下载页面内容


import re
import requests
from bs4 import BeautifulSoup


"""
@description: 存为 page.html 文件
-------
@param:
-------
@return:
"""
def save_as_html(html_content):
    try:
        f = open("page.html", mode="w",encoding="utf-8")
        html_content = BeautifulSoup(html_content, "html.parser").prettify()
        f.write(str(html_content))
        f.close()
    except Exception as e:
        print(e)

"""
@description: 从输入的字符串中提取地址
-------
@param:
-------
@return:
"""
def get_url():
    # input the url
    input_str = input("The url:")
    if ("http" not in input_str):
        input_str = "https://" + input_str
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_str)
    return url[0]

"""
@description: 获取页面内容源码
-------
@param:
-------
@return:
"""
def get_html_content(url):
    try:
        r = requests.get(url, timeout=5)
        r.encoding = "UTF-8"
        if (r.status_code == 200):
            return r.text
        else:
            return ""
    except Exception as e:
        print(e)


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    url = get_url()
    if (url != ""):
        html_content = get_html_content(url)
        save_as_html(html_content)
    else:
        print("The URL is not reasonable!")

    
