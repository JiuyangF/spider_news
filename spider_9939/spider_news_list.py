# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 2:58 PM
# @Author  : jiuyang
# @File    : spider_9939_news.py
import requests
from Spider.spider_9939.run import UA
from lxml import etree


def merge_news_info(page_content):
    """
    用xpath 格式化数据
    :param page_content:    获取到的新闻列表页内容
    :return:
    """
    news_list = []
    new_dict = {}

    s_tree = etree.HTML(page_content)

    # 获取到文章的<a>标签中的文章列表数据
    news_content = s_tree.xpath('//a[@class="m_listone-right-title"]')

    for one_new in news_content:
        new_dict['title'] = one_new.text
        new_dict['url'] = one_new.attrib['href']
        news_list.append(new_dict)

    return news_list


def get_news_lists(session, page_num):
    """
    获取文章列表
    :param url:    str    网站url"http://news.9939.com/hrsz/2.shtml"
    :param page_num: int   需要爬取的文章页数
    :return:all_news_list   list_dict   文章列表
    """
    all_news_list = []
    for i in range(1, page_num + 1):
        page_url = 'http://news.9939.com/hrsz/%s.shtml' % str(i)
        respond = session.get(page_url)

        # 调用格式化文章列表数据的函数 返回文章列表
        news_list = merge_news_info(respond.content.decode('utf-8'))
        print(news_list)
        all_news_list.extend(news_list)
    return all_news_list


def save_all_news_list(env, all_news_list):
    """
    文章列表数据入库
    :param env:    入库配置
    :param all_news_list:    文章列表
    :return:
    """
    pass


if __name__ == '__main__':
    session = requests.session()
    session.headers['User-Agent'] = UA

    all_news_list = get_news_lists(session, 1)
    save_all_news_list('dev',all_news_list)
