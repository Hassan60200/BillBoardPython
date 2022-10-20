import scrapy


class MangasplusSpider(scrapy.Spider):
    name = 'mangasPlus'
    allowed_domains = ['mangaplus.shueisha.co.jp']
    start_urls = ['http://mangaplus.shueisha.co.jp/']

    def parse(self, response):
        pass
