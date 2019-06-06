# -*- coding: utf-8 -*-
import scrapy
from mk11_galec.items import Mk11GalecItem


class Mk11galecSpider(scrapy.Spider):
    name = 'Mk11Galec'
    allowed_domains = ['culture.leclerc']
    start_urls = ['https://bit.ly/2DPSvGz', # ps4 standard
                  'https://bit.ly/2Y40w2v', # ps4 premium
                  'https://bit.ly/2IYxptR', # ps4 kollector
                  'https://bit.ly/2Y9htbB', # xone standard
                  'https://bit.ly/2LoofsR', # xone premium
                  'https://bit.ly/2Y7nKow', # xone kollector
                  'https://bit.ly/2LnifR6', # switch
                  'https://bit.ly/2Y8LEj8', # pc kollector
                 ]

    def parse(self, response):
        items = Mk11GalecItem()
        title = response.xpath('//h1[@class="ProductDetails-title"]/span[@property="name"]/text()').extract()
        platform = response.xpath('//*[@id="voirlescaracs"]/div/div[5]/span[2]/text()').extract()
        sale_price = response.xpath('//span[@property="price"]/text()').extract()
        items["product_name"] = "".join(title).strip()
        items["product_platform"] = ",".join(map(lambda x: x.strip(), platform)).strip()
        items["product_sale_price"] = "".join(sale_price).strip()
        yield items
