# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BillboardItem(scrapy.Item):
    # define the fields for your item here like:
        rank = scrapy.Field()
        img = scrapy.Field()
        title = scrapy.Field()
        singer = scrapy.Field()
        last_position = scrapy.Field()
        peak_position = scrapy.Field()
        weaks_on_charts = scrapy.Field()
   
