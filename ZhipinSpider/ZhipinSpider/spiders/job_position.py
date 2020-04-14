# -*- coding: utf-8 -*-
import scrapy
from ZhipinSpider.items import ZhipinspiderItem

class JobPositionSpider(scrapy.Spider):
    #定义该sprider的名字
    name = 'job_position'
    #定义该sprider允许爬取的域名
    allowed_domains = ['zhipin.com']
    #定义该sprider允许爬取的首页列表
    start_urls = ['https://www.zhipin.com/job_detail/?query=%E6%B5%8B%E8%AF%95&city=101270100&industry=&position=']

    #提取response所包含的信息
    def parse(self, response):
        for job_primary in response.xpath('//div[@class="job_primary"]'):
            item = ZhipinspiderItem()
            info_primary = job_primary.xpath('./div[@class="info_primary"]')
            item['title'] = info_primary.xpath('./h3/a/div[@class="job_title"]/text()').extract_first()

            yield item

