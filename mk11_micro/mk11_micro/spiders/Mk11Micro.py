# -*- coding: utf-8 -*-
import scrapy
from mk11_micro.items import Mk11MicroItem


class Mk11microSpider(scrapy.Spider):
    name = 'Mk11Micro'
    allowed_domains = ['micromania.fr']
    start_urls = ['https://www.micromania.fr/mortal-kombat-11-93852.html', # ps4 steelbook
                 'https://www.micromania.fr/mortal-kombat-11-premium-edition-93858.html', # ps4 premium
                 'https://www.micromania.fr/mortal-kombat-11-edition-kollector-94700.html', # ps4 kollector
                 'https://www.micromania.fr/mortal-kombat-11-93854.html', # xone steelbook
                 'https://www.micromania.fr/mortal-kombat-11-premium-edition-93859.html', # xone premium
                 'https://www.micromania.fr/mortal-kombat-11-edition-kollector-94701.html', # xone kollector
                 'https://www.micromania.fr/mortal-kombat-11-93856.html', # switch
                 ]

    def parse(self, response):
        items = Mk11MicroItem()
        title = response.xpath('//h1[@itemprop="name"]/text()').extract()
        platform = response.xpath('//div[@class="desktop"]//p[@class="platform"]/text()').extract()
        sale_price = response.xpath('//*[@id="product-price-1"]/span/text()').extract()
        items["product_name"] = "".join(title).strip()
        items["product_platform"] = ",".join(map(lambda x: x.strip(), platform)).strip()
        items["product_sale_price"] = "".join(sale_price).strip()
        yield items


# //span[@class="price"]
# //*[@id="product-price-1"]/span