# -*- coding: utf-8 -*-
import scrapy
from mk11_fnac.items import Mk11FnacItem


class Mk11fnacSpider(scrapy.Spider):
    name = 'Mk11Fnac'
    allowed_domains = ['fnac.com']
    # custom_settings = {'HTTPPROXY_ENABLED': True}
    start_urls = ['https://fnac.com/a13162174', # ps4 standard
                  'https://fnac.com/a13162176/', # ps4 premium
                  'https://fnac.com/a13276126/', # ps4 kollector
                  'https://fnac.com/a13162175', # xone standard
                  'https://fnac.com/a13162177/', # xone premium
                  'https://fnac.com/a13276127', # xone kollector
                  'https://fnac.com/a13162178', # switch standard
                  'https://fnac.com/a13276128' # pc kollector
                  ]

    def parse(self, response):
        items = Mk11FnacItem()
        title = response.xpath('//h1[@class="f-productHeader-Title"]/text()').extract()
        platform = response.xpath('/html/body/div[2]/div[1]/div[1]/section[1]/div[1]/span[1]/text()').extract()
        sale_price = response.xpath('//*[@class="f-priceBox-price f-priceBox-price--reco checked"]/text()').extract()
        items["product_name"] = "".join(title).strip()
        items["product_platform"] = ",".join(map(lambda x: x.strip(), platform)).strip()
        items["product_sale_price"] = "".join(sale_price).strip()
        yield items


