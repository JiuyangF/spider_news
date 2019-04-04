# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 3:02 PM
# @Author  : jiuyang
# @File    : run.py
import requests

COOKIES_MAC = {}

UA = 'Mozilla/5.0 (Linux; Android 8.0.0; MIX 2 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/564 MMWEBSDK/190102 Mobile Safari/537.36 MMWEBID/4989 MicroMessenger/7.0.3.1400(0x2700033A) Process/toolsmp NetType/WIFI Language/zh_CN'


def form_session():
    session = requests.session()
    session.headers['User-Agent'] = UA
    requests.utils.cookiejar_from_dict(COOKIES_MAC, session.cookies)
    # 初始化session
    return session


if __name__ == '__main__':
    pass