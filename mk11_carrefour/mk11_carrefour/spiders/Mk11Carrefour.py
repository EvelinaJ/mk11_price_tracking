# -*- coding: utf-8 -*-
import scrapy
from mk11_carrefour.items import Mk11CarrefourItem


class Mk11carrefourSpider(scrapy.Spider):
    name = 'Mk11Carrefour'
    allowed_domains = ['carrefour.fr']
    start_urls = ['https://bit.ly/2DQ5Tuk', # ps4 standard
                  'https://bit.ly/2ZSufgB', # xone standard
                  'https://bit.ly/2Hbq9aK' # switch standard
                 ]

    def parse(self, response):
        items = Mk11CarrefourItem()
        title = response.xpath(
        	'//*[@id="product-detail-page"]/div[1]/div/div/div/div/div[3]/div/div[1]/div[1]/h1/text()'
        	).extract()
        # platform = response.xpath('//*[@id="voirlescaracs"]/div/div[5]/span[2]/text()').extract()
        sale_price = response.xpath(
        	'//*[@id="product-detail-page"]/div[1]/div/div/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div/span/text()'
            ).extract()
        items["product_name"] = "".join(title).strip()
        # items["product_platform"] = ",".join(map(lambda x: x.strip(), platform)).strip()
        items["product_sale_price"] = "".join(sale_price).strip()
        yield items


