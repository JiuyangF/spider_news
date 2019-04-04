# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 3:02 PM
# @Author  : jiuyang
# @File    : spider_news_content.py
import requests
from lxml import etree

from spider_9939.run import UA


class NewContent(object):
    def __init__(self, session, url, title=''):
        self.session = session
        # self.title = title
        self.url = url

        self.art_content = ''
        self.s_tree = None
        self.img_urls = []
        # self.read_num = 0
        # self.like_num = 0
        # self.comment_json = ''
        # self.comment_id = ''
        # self.pub_time = ''

    def __repr__(self):
        return ('url: %s \nimg_urls %s' % (self.url, self.img_urls))

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
        self.get_news_content()
        if self.art_content.find('此内容因违规无法查看') >= 0 or self.art_content.find(
                '此内容被投诉且经审核涉嫌侵权') >= 0 or self.art_content.find('该内容已被发布者删除') >= 0:
            self.art_content = '涉嫌违规，不予展示'
            print(self.url)
            return
        self.get_img_urls()


if __name__ == '__main__':
    session = requests.session()
    session.headers['User-Agent'] = UA

    ac = NewContent(url='http://news.9939.com/hrsz/2019/0228/4724680.shtml',
                    session=session)
    ac.run()
    print(ac)
