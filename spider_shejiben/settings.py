# -*- coding: utf-8 -*-
# @Time    : 2019-11-20 5:45 PM
# @Author  : jiuyang
# @File    : settings.py
from fake_useragent import UserAgent
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

UA = UserAgent()

URL = 'https://www.shejiben.com/order_lobby/?city=beijing'
# URL = 'https://www.shejiben.com/order_lobby/?city=beijing'city=beijing&
DETAIL_URL = "https://www.shejiben.com/order_lobby/order.php?id=%s"

HAVE_SEND_CODE = {}
SEND_TIMES = 30
