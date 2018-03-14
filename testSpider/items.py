# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItem(scrapy.Item):
    title_name= scrapy.Field()
    public_time = scrapy.Field()
    good_num = scrapy.Field()
    collect_num = scrapy.Field()
    comment_num = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()

    # 保存图片的路径
    image_path= scrapy.Field()
    # 使用md5对url进行加密
    url_object_id = scrapy.Field()