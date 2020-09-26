#!/usr/bin/env python
#-*- coding:utf-8 -*

import requests
import re
from bs4 import BeautifulSoup

def saveAsHtml(htmlContent):
    try:
        f = open("page.html",mode="w",encoding="utf-8")
        htmlContent = BeautifulSoup(htmlContent,"html.parser").prettify()
        f.write(str(htmlContent))
        f.close()
    except Exception as e:
        print(e)


def getUrl():
    # input the url
    inputStr = input("The url:")
    if("http" not in inputStr):
        inputStr = "https://" + inputStr
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', inputStr)
    return url[0]

def getHtmlContent(url):
    try:
        r = requests.get(url,timeout=5)
        if(r.status_code == 200):
            return r.text
        else:
            return ""
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = getUrl()
    if(url != ""):
        htmlContent = getHtmlContent(url)
        saveAsHtml(htmlContent)
    else:
        print("The URL is not reasonable!")

    
