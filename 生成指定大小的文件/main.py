#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/kantan-tools/生成指定大小的文件/main.py
# @DATE: 2021/01/19 Tue
# @TIME: 17:21:11
#
# @DESCRIPTION: 生成指定大小的文件


import os
import random


"""
@description: 生成指定大小的文件
-------
@param:
-------
@return:
"""
def gen_size_file(file_name, file_size):
    # file path
    file_path = file_name
    file = open(file_path, 'w')
    file.seek(file_size)
    file.write('\x00')
    file.close()
    print("done!")

"""
@description: 从输入中获取所需生成文件的大小
-------
@param:
-------
@return:
"""
def get_file_size():
    # start here
    file_name = input("The file name you need:")
    file_size = input("The size you need:").lower().replace("b", "")
    # size
    if ("k" in file_size):
        file_size = int(file_size.replace("k", ""))*1024
    elif("m" in file_size):
        file_size = int(file_size.replace("m",""))*1024*1024
    elif("g" in file_size):
        file_size = int(file_size.replace("g",""))*1024*1024*1024
    else:
        file_size = int(file_size)*1024
    return file_name, file_size

"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    file_name, file_size = get_file_size()
    try:
        print("FileSize:"+str(file_size)+"kb!building...")
        gen_size_file(file_name, file_size)
    except Exception as e:
        print(e)