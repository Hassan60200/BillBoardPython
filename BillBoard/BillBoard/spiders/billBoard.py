import scrapy


class BillboardSpider(scrapy.Spider):
    name = 'billBoard'
    allowed_domains = ['www.billboard.com']
    start_urls = ['http://www.billboard.com/']

    def parse(self, response):
        pass
