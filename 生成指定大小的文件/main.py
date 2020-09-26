#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random

def genSizeFile(fileName, fileSize):
    #file path
    filePath=fileName
    # ========== mode1 =========
    # date size
    # ds=0
    # with open(filePath, "w", encoding="utf8") as f:
    # while ds<fileSize:
    # f.write(str(round(random.uniform(-1000, 1000),2)))
    # f.write("\n")
    # ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))
    # ========== mode2 =========
    file = open(filePath,'w')
    file.seek(fileSize)
    file.write('\x00')
    file.close()
    print("done!")

def getFileSize():
    # start here.
    fileName = input("The file name you need:")
    fileSize = input("The size you need:").lower().replace("b","")
    # size
    if("k" in fileSize):
        fileSize = int(fileSize.replace("k",""))*1024
    elif("m" in fileSize):
        fileSize = int(fileSize.replace("m",""))*1024*1024
    elif("g" in fileSize):
        fileSize = int(fileSize.replace("g",""))*1024*1024*1024
    else:
        fileSize = int(fileSize)*1024
    return fileName,fileSize


if __name__ == "__main__":
    fileName,fileSize = getFileSize()
    try:
        print("FileSize:"+str(fileSize)+"kb!building...")
        genSizeFile(fileName,fileSize)
    except Exception as e:
        print(e)