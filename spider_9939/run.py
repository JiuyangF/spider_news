# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 3:02 PM
# @Author  : jiuyang
# @File    : run.py
import requests

from spider_9939.settings import UA
from spider_9939.spider_news_content import NewContent
from spider_9939.spider_news_list import get_news_lists


def run(page_num):
    session = requests.session()
    session.headers['User-Agent'] = UA
    # 所有文章中的图片url
    all_img_url = []

    # 获取文章的列表
    all_news_list = get_news_lists(session, page_num)

    # 获取文章内容
    for art_info in all_news_list:
        url = art_info['url']
        ac = NewContent(url=url,
                        session=session)
        ac.run()
        # print(ac)
        all_img_url.extend(ac.img_urls)
    print(all_img_url)


if __name__ == '__main__':
    run(2)
