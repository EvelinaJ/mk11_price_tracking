# -*- coding: utf-8 -*-
import scrapy
from mk11_auchan.items import Mk11AuchanItem


class Mk11auchanSpider(scrapy.Spider):
    name = 'Mk11Auchan'
    allowed_domains = ['auchan.fr']
    start_urls = ['https://www.auchan.fr/p-c1099806', # ps4 standard
                  'https://www.auchan.fr/p-c1099851', # ps4 premium
                  'https://www.auchan.fr/p-c1099863', # ps4 kollector
                  'https://www.auchan.fr/p-c1099830', # xone standard
                  'https://www.auchan.fr/p-c1099862', # xone premium
                  'https://www.auchan.fr/p-c1099873', # xone kollector
                  'https://www.auchan.fr/p-c1099874', # switch standard
                 ]

    def parse(self, response):
        items = Mk11AuchanItem()
        title = response.xpath('//h1[@class="product-detail--title"]/text()').extract()
        platform = response.xpath('//*[@id="tabTechnical"]/main/div/ul/li[5]/div/span/text()').extract()
        sale_price = response.xpath('//*[@id="onlineContent"]/div[1]/div/div/div/span/text()').extract()
        items["product_name"] = "".join(title).strip()
        items["product_platform"] = ",".join(map(lambda x: x.strip(), platform)).strip()
        items["product_sale_price"] = "".join(sale_price).strip()
        yield items


