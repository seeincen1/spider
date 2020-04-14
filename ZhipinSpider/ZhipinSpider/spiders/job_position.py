# -*- coding: utf-8 -*-
import scrapy


class JobPositionSpider(scrapy.Spider):
    #定义该sprider的名字
    name = 'job_position'
    #定义该sprider允许爬取的域名
    allowed_domains = ['zhipin.com']
    #定义该sprider允许爬取的首页列表
    start_urls = ['http://zhipin.com/']

    #提取response所包含的信息
    def parse(self, response):
        pass
