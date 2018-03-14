# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re

from  scrapy.loader import  ItemLoader
from  scrapy.loader.processors import  TakeFirst,MapCompose
from  testSpider.Tools.common import get_MD5


class TestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def deal_datestr(value):
    try:
        create_time = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_time = datetime.datetime.now().date()

    return create_time

def deal_num(value):
    r = re.findall('.*?(\d+).*', value)
    if len(r):
        num = int(r[0])
    else:
        num = 0
    return num

def return_value(value):
    return value

def return_MD5str(value):
    return get_MD5(value)


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ArticleItem(scrapy.Item):
    title_name= scrapy.Field()
    public_time = scrapy.Field(

        # 对传入的值进行预处理
        input_processor= MapCompose(deal_datestr)
    )
    good_num = scrapy.Field(
        input_processor=MapCompose(deal_num)
    )
    collect_num = scrapy.Field(
        input_processor = MapCompose(deal_num)
    )
    comment_num = scrapy.Field(
        input_processor=MapCompose(deal_num)
    )
    content = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )

    # 保存图片的路径
    image_path= scrapy.Field()
    # 使用md5对url进行加密
    url_object_id = scrapy.Field(
        input_processor = MapCompose(return_MD5str)
    )
