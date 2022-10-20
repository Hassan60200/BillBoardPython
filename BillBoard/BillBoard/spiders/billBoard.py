import scrapy
from scrapy import Request
from BillBoard.items import BillboardItem

class BillboardSpider(scrapy.Spider):
    name = 'billBoard'
    allowed_domains = ['www.billboard.com']
    start_urls = ['https://www.billboard.com/charts/billboard-global-200/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_song)

    def parse_song(self, response):
        liste_song = response.css('.o-chart-results-list-row-container')
        
        for song in liste_song:
            item = BillboardItem()
            
            # Rank de la musique
            try:
                item['rank'] = song.css('li.o-chart-results-list__item span::text')[0].extract().strip()
            except:
                item['rank'] = 'None'
                
            # img de la musique
            try:
                item['img'] = song.css('li.o-chart-results-list__item img.c-lazy-image__img.lrv-u-background-color-grey-lightest.lrv-u-width-100p.lrv-u-display-block.lrv-u-height-auto').attrib['data-lazy-src']
            except:
                item['img'] = 'None'
            
            # title de la musique
            try:
                item['title'] = song.css('li.o-chart-results-list__item h3::text')[0].extract().strip()
            except:
                item['title'] = 'None'
            
            # singer de la musique
            try:
                item['singer'] = song.css('li.lrv-u-width-100p span.c-label::text').get().strip()
            except:
                item['singer'] = 'None'
            
            yield item