#!/usr/bin/env python
# -*- coding:UTF-8 -*-


import re
import requests
from bs4 import BeautifulSoup


def save_as_html(html_content):
    try:
        f = open("page.html", mode="w",encoding="utf-8")
        html_content = BeautifulSoup(html_content, "html.parser").prettify()
        f.write(str(html_content))
        f.close()
    except Exception as e:
        print(e)

def get_url():
    # input the url
    input_str = input("The url:")
    if ("http" not in input_str):
        input_str = "https://" + input_str
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_str)
    return url[0]

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

# main
if __name__ == "__main__":
    url = get_url()
    if (url != ""):
        html_content = get_html_content(url)
        save_as_html(html_content)
    else:
        print("The URL is not reasonable!")

    
