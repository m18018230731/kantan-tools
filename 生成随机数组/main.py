#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/kantan-tools/生成随机数组/main.py
# @DATE: 2021/01/19 Tue
# @TIME: 17:22:20
#
# @DESCRIPTION: 生成随机数组以供测试使用


import random


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    try:
        start_num = int(input("Start number:"))
        need_num = int(input("How much u need:"))
        result_list = []
        for i in range(need_num):
            result_list.append(start_num)
            start_num = start_num + random.randint(-1000, 1000)
        print(result_list)
    except Exception as e:
        print(e)