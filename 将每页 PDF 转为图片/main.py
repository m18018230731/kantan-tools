#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/kantan-tools/将每页 PDF 转为图片/main.py
# @DATE: 2021/03/10 Wed
# @TIME: 17:49:47
#
# @DESCRIPTION: PDF 转图片


import sys
import fitz
from PIL import Image


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
@description: 将图片切割为左右两份
-------
@param:
-------
@return:
"""
def cut_image(image, image_file_name, count):
    # 创建切割后图片存储用列表
    width, height = image.size
    item_width = int(width/count)
    item_height = height
    box_list = []
    for i in range(0, count):
        box = (i*item_width, 0, (i+1)*item_width, item_height)
        box_list.append(box)
    # 图片切割
    image_list = [image.crop(box) for box in box_list]
    # 保存图片
    for image_index, image in enumerate(image_list):
        image.save("图片/切割后/" + image_file_name + "-" + str(image_index) \
                    + ".png", "PNG")

"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    # PDF 每页转储为图片
    pdf_file_name = sys.argv[1]
    if (".pdf" not in pdf_file_name):
        pdf_file_name = pdf_file_name + ".pdf"
    pdf_file = get_pdf_file(pdf_file_name)
    print("PDF 总共有：" + str(pdf_file.pageCount) + " 页。")
    try:
        for page_no in range(0, pdf_file.pageCount):
            page = pdf_file.loadPage(page_no)
            pix = page.getPixmap()
            pix.writePNG("图片/" + str(page_no) + ".png")
            # 图片从中间横向切割为 2 份
            cut_image(
                Image.open("图片/" + str(page_no) + ".png"), str(page_no), 2)
    except Exception as e:
        print("PDF 每页转储为图片并切割时出错：" + str(e))
    finally:
        pdf_file.close()
    print("PDF 每页转储为图片并切割完成！ ")