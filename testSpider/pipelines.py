# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from  scrapy.pipelines.images import ImagesPipeline

class TestspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # 可以通过重载获取图片的存储地址

        # 打断点可以知道,results是一个list,其中每个元素又是一个tuple,每个tuple有两个元素,一个时bool类型,一个时字典类型,所存放图片路径的字符串就在字典类型的path键值对的值
        for ok,value in results:
            image_file_path = value['path']

        item['image_path'] = image_file_path

        # 最后别忘了返回item
        return  item