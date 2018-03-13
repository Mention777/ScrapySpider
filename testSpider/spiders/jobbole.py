# -*- coding: utf-8 -*-
import scrapy
import  re
from urllib import  parse
from scrapy.http import Request

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://python.jobbole.com/all-posts/']

    """
    1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
    2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
    """

    def parse(self, response):

        post_nodes = response.xpath('//div[@id = "archive"]/div[@class = "post floated-thumb"]/div[@class = "post-thumb"]/a')
        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
        for post_node in post_nodes:
            image_url = post_node.xpath('img/@src').extract_first("")
            post_url = post_node.xpath('@href').extract_first("")
            yield Request(url=parse.urljoin(response.url,post_url),meta={'front_image_url':image_url},callback=self.parse_detail,dont_filter=True)

        # 提取下一页并交给scrapy进行下载
        next_page = response.xpath('//a[@class = "next page-numbers"]/@href').extract_first("")

        if next_page :
            yield Request(url=parse.urljoin(response.url,next_page),callback=self.parse,dont_filter=True)


    def parse_detail(self,response):
        '''
        通过Xpath获取html内所有需要的字段内容
        '''


        # 文章标题
        title_name = response.xpath('//div[@class = "entry-header"]/h1/text()').extract_first("")

        # 发布日期
        public_time = response.xpath('//p[@class = "entry-meta-hide-on-mobile"]/text()').extract_first("").strip().replace('·','').strip()

        # 点赞数
        good_num = response.xpath('//*[@class =" btn-bluet-bigger href-style vote-post-up   register-user-only "]/h10/text()').extract_first("")
        # 收藏数
        collect_num= response.xpath('//span[contains(@data-site-id,"13")]/text()').extract_first("").strip()
        r = re.findall('.*?(\d+).*',collect_num)
        if len(r):
            collect_num = int(r[0])
        else:
            collect_num = 0

        # 评论数
        comment_num = response.xpath('//span[@class = "btn-bluet-bigger href-style hide-on-480"]/text()').extract_first("").strip()
        r = re.findall('.*?(\d+).*', comment_num)
        if len(r):
            comment_num = int(r[0])
        else:
            comment_num = 0

        # 文章内容
        content = response.xpath("//div[@class='entry']").extract_first("")
        a = 1
