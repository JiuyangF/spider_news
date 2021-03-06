# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 3:02 PM
# @Author  : jiuyang
# @File    : spider_news_content.py
import requests
from lxml import etree

from spider_9939.settings import UA


class NewContent(object):
    def __init__(self, session, url, title=''):
        self.session = session
        # self.title = title
        self.url = url

        self.art_content = ''   # 清洗后的文章内容
        self.s_tree = None  # 文章的xpath tree
        self.img_urls = []  # 文章中的图片url列表
        # self.read_num = 0
        # self.like_num = 0
        # self.comment_json = ''
        # self.comment_id = ''
        # self.pub_time = ''

    def __repr__(self):
        return 'url: %s \nimg_urls %s' % (self.url, self.img_urls)

    @property
    def clear_content(self):
        """获取文章内容"""
        primary_inner = self.s_tree.xpath('//div[@class="article-content"]//text()')
        return '\n'.join(primary_inner).strip()

    def get_news_content(self):
        """获取文章内容"""
        response = self.session.get(self.url)
        art_content_html = response.content.decode('utf-8')
        self.s_tree = etree.HTML(art_content_html)
        self.art_content = self.clear_content.strip()

    def get_img_urls(self):
        img_inn = self.s_tree.xpath('//div[@class="article-content"]//img')
        for img_a in img_inn:
            self.img_urls.append(img_a.attrib['src'])

    def run(self):
        try:
            self.get_news_content()
            if self.art_content == '':
                self.art_content = '404'
                print("获取文章内容为空%s" % self.url)
                return
            # print(self.art_content)
            self.get_img_urls()
        except Exception as a:
            print(a)


if __name__ == '__main__':
    session = requests.session()
    session.headers['User-Agent'] = UA

    ac = NewContent(url='http://news.9939.com/hrsz/2019/0308/4726322.shtml',
                    session=session)
    ac.run()
    print(ac)
