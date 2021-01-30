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
import requests
from urllib.parse import urlparse


# 部分订阅获取不到的情况使用代理
proxy = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080"
}


"""
@description: 从 TXT 文件中获取订阅地址
-------
@param:
-------
@return: <list>
"""
def get_subscription_urls():
    subscription_urls = []
    if (not subscription_urls):
        txt = open("ssr.txt", "r")
        for line in txt.readlines():
            subscription_urls.append(line.strip())
    return subscription_urls

"""
@description: 获取订阅的原始信息
-------
@param:
-------
@return:
"""
def get_subscription_origin_infos(subscription_urls, use_proxy_flg=False):
    subscription_origin_infos = []
    for subscription_url in subscription_urls:
        try:
            # 默认 30 秒超时
            if (use_proxy_flg):
                response = requests.get(subscription_url,
                                        proxies=proxy,
                                        timeout=30)
            else:
                response = requests.get(subscription_url,
                                        timeout=30)
            subscription_origin_infos.append(response.text)
        except Exception as e:
            print(subscription_url + " 获取订阅原始信息出错！" \
                  + "\r\n出错信息：" + str(e))
            break
    return subscription_origin_infos

"""
@description: BASE64 解码的封装
-------
@param:
-------
@return:
"""
def my_b64decode(str_4_b64decode):
    # 带 - 需要用专用的 URL BASE64 解码
    if ("-" in str_4_b64decode):
        # 最多加 4 次 "=" 以使原始信息符合 BASE64 格式
        for i in range(0, 4):
            try:
                str_after_b64decode = base64.urlsafe_b64decode(str_4_b64decode)
                break
            except Exception:
                str_4_b64decode = str_4_b64decode + "="
    # 不包含 - 则试用普通的 BASE64 解码即可
    else:
        # 最多加 4 次 "=" 以使原始信息符合 BASE64 格式
        for i in range(0, 4):
            try:
                str_after_b64decode = base64.b64decode(str_4_b64decode)
                break
            except Exception:
                str_4_b64decode = str_4_b64decode + "="
    return str_after_b64decode

"""
@description: 从订阅原始信息中拆分出每条 SSR 的原始信息
-------
@param:
-------
@return:
"""
def get_ssr_origin_infos(subscription_origin_infos):
    ssr_origin_infos = []
    for subscription_origin_info in subscription_origin_infos:
        # BASE64 解码
        subscription_info = my_b64decode(subscription_origin_info)
        # UTF-8 编码
        subscription_info = subscription_info.decode("UTF-8")
        # 根据换行符分行
        ssr_origin_infos_4_base64decode = subscription_info.split("\n")
        for ssr_origin_info_4_base64decode in ssr_origin_infos_4_base64decode:
            # 去掉最后一个分割出来的空字符
            if (ssr_origin_info_4_base64decode):
                info_4_base64decode = ssr_origin_info_4_base64decode \
                                        .replace("ssr://", "") \
                                        .replace("_", "/") \
                                        .replace("-", "+")
                try:
                    ssr_origin_info = my_b64decode(
                        info_4_base64decode).decode("UTF-8")
                    ssr_origin_infos.append(ssr_origin_info)
                except Exception:
                    print("SSR 原始信息 BASE64 解码失败：" \
                          + ssr_origin_info_4_base64decode)
                    continue
    return ssr_origin_infos

"""
@description: 解析 SSR 原始信息以获取具体的代理信息
-------
@param:
-------
@return:
"""
def parse_ssr_origin_info(ssr_origin_info):
    # === SSR 基础信息 ===
    # 服务器 IP
    ssr_ip = ssr_origin_info.split("/?")[0].split(":")[0]
    # 服务器端口
    ssr_port = ssr_origin_info.split("/?")[0].split(":")[1]
    # 密码
    ssr_password = my_b64decode(ssr_origin_info.split("/?")[0].split(":")[5]) \
                    .decode("UTF-8")
    # 加密（chacha20 加密 https://www.icode9.com/content-4-224432.html）
    ssr_method = ssr_origin_info.split("/?")[0].split(":")[3]
    # 协议
    ssr_protocol = ssr_origin_info.split("/?")[0].split(":")[2]
    # 混淆
    ssr_obfs = ssr_origin_info.split("/?")[0].split(":")[4]
    # === SSR 进阶参数 ===
    # 混淆参数
    ssr_obfs_param = my_b64decode(ssr_origin_info.split("/?")[1].split("&")[0] \
                        .split("=")[1]).decode("UTF-8")
    # 协议参数
    ssr_protocol_param = my_b64decode(ssr_origin_info.split("/?")[1] \
                            .split("&")[1].split("=")[1]).decode("UTF-8")
    # === SSR 其他信息 ===
    # 备注
    try:
        ssr_remarks = my_b64decode(ssr_origin_info.split("/?")[1]
                        .split("&")[2].split("=")[1]).decode("UTF-8")
    except Exception:
        ssr_remarks = ""
    # 分组
    try:
        ssr_group = my_b64decode(ssr_origin_info.split("/?")[1].split("&")[3] \
                        .split("=")[1]).decode("UTF-8")
    except Exception:
        ssr_group = ""
    # udpport
    try:
        ssr_udpport = ssr_origin_info.split("/?")[1].split("&")[4].split("=")[1]
    except Exception:
        ssr_udpport = ""
    # uot
    try:
        ssr_uot = ssr_origin_info.split("/?")[1].split("&")[5].split("=")[1]
    except Exception:
        ssr_uot = ""
    # 拼接
    ssr_info = {
        "ip": ssr_ip,
        "port": ssr_port,
        "password": ssr_password,
        "method": ssr_method,
        "protocol": ssr_protocol,
        "protocol_param": ssr_protocol_param,
        "obfs": ssr_obfs,
        "obfs_param": ssr_obfs_param,
        "remarks": ssr_remarks,
        "group": ssr_group,
        "udpport": ssr_udpport,
        "uot": ssr_uot
    }
    return ssr_info


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    # 获取 SSR 订阅的原始信息并解码
    subscription_urls = get_subscription_urls()
    subscription_origin_infos = get_subscription_origin_infos(subscription_urls,
                                                              True)
    # 从订阅原始信息中拆分出每条 SSR 的原始信息
    ssr_origin_infos = get_ssr_origin_infos(subscription_origin_infos)
    # 逐条解析 SSR，以获得具体信息
    for ssr_origin_info in ssr_origin_infos:
        print(parse_ssr_origin_info(ssr_origin_info))
