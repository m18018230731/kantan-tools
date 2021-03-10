#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/kantan-tools/将每页 PDF 转为图片/main.py
# @DATE: 2021/03/10 Wed
# @TIME: 17:49:47
#
# @DESCRIPTION: PDF 转图片


import fitz


"""
@description: 获取 PDF 文件
-------
@param:
-------
@return:
"""
def get_pdf_file(pdf_file_path):
    return fitz.open(pdf_file_path)

"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    pdf_file = get_pdf_file("单词.pdf")
    for page_no in range(0, 37):
        page = pdf_file.loadPage(page_no)
        pix = page.getPixmap()
        pix.writePNG(str(page_no) + ".png")