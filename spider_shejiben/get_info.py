# -*- coding: utf-8 -*-
# @Time    : 2019-11-20 5:57 PM
# @Author  : jiuyang
# @File    : get_info.py
import datetime
import time
from lxml import etree

import requests
import json
import re
import random

# from mail_helper import MyEmail
from settings import URL, UA, HAVE_SEND_CODE, SEND_TIMES, DETAIL_URL

from mail_helper import send

to_user = ["shejiben_sunfuss@163.com", "sunfuss@126.com"]  # "shejiben_sunfuss@163.com","yangjt@knowbox.cn",
# to_user = ["yangjt@knowbox.cn"]  # "shejiben_sunfuss@163.com","yangjt@knowbox.cn",


def merge_news_info(page_content):
    """
    用xpath 格式化数据
    :param page_content:    获取到的新闻列表页内容
    :return:
    """
    news_list = []

    s_tree = etree.HTML(page_content)

    # 获取到文章的<a>标签中的文章列表数据
    news_content = s_tree.xpath('//div[@class="_info"]')
    message = ""
    for one_new in news_content:
        try:
            price = one_new.xpath('.//span[@class="price"]')[0].text
            price = re.sub(r'[\u4e00-\u9fa5]', '', price)
            if '-' in price:
                low_price = int(price.split('-')[0])
            else:
                low_price = int(price)
            if low_price < 10000:
                continue
            title = one_new.xpath('.//a')[0].text
            href = one_new.xpath('.//a/@href')[0]
            shejiben_id = re.findall('id=(\d+)', href)[0]
            print("符合预期的信息", shejiben_id, title, price)
            code_use = HAVE_SEND_CODE.get(shejiben_id, 0)
            if code_use > SEND_TIMES:
                continue
            url = DETAIL_URL % shejiben_id
            message += """
            <a href="{}">{}</a><br>
            标题：{}<br>
            价格：{}<br>
            """.format(url, url, title, price)
        except Exception as e:
            print("解析网页错误%s" % e)
            continue
    print("finish", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    if message:
        send(message, to_user)
    print("邮件发送完成")
    return news_list


def get_show():
    while True:
        headers = {
            "content-length" : "124",
            "user-agent"     : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "content-type"   : "application/x-www-form-urlencoded; charset=UTF-8",
            "accept-encoding": "gzip, deflate, br",
            "referer"        : "https://www.shejiben.com/order_lobby/?city=beijing"
        }
        try:
            x = random.randint(0, 3)
            if x == 0:
                headers['user-agent'] = UA.chrome
            elif x == 1:
                headers['user-agent'] = UA.firefox
            else:
                headers['user-agent'] = UA.safari
            data = json.dumps({"city": "beijing"})
            res = requests.post(URL, data, headers=headers)
            res_c = res.content.decode('utf-8')
            # print(res_c)
            merge_news_info(res_c)
        except Exception as e:
            print("主程序报错 %s" % e)
        time.sleep(random.randint(10, 30))


if __name__ == '__main__':
    get_show()
    # s = "https://www.shejiben.com/order_lobby/order.php?id=339892"
    #
    # x = re.findall('id=(\d+)"', s)[0]
    #
