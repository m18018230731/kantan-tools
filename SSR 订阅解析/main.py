#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: E:\Github\kantan-tools\SSR 订阅解析\main.py
# @DATE: 2021/01/30 周六
# @TIME: 13:23:19
#
# @DESCRIPTION: SSR 订阅解析


import base64
from urllib.parse import urlparse


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    ssr_text = ""
    try:
        ssr_text = ssr_text + "=="
        print(base64.b64decode(ssr_text).decode("UTF-8"))
        print(base64.b64decode("").decode("UTF-8"))
        print(base64.b64decode("").decode("UTF-8"))
        print(base64.b64decode("").decode("UTF-8"))
        print(base64.urlsafe_b64decode("").decode("UTF-8"))
        print(base64.urlsafe_b64decode("").decode("UTF-8"))
    except Exception as e:
        print(e)