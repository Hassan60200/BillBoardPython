import scrapy
from scrapy import Request
from BillBoard.items import BillboardItem

class BillboardSpider(scrapy.Spider):
    name = 'billBoard'
    allowed_domains = ['www.billboard.com']
    start_urls = ['https://www.billboard.com/charts/billboard-global-200/','https://www.billboard.com/charts/r-and-b-songs/','https://www.billboard.com/charts/hot-100/','https://www.billboard.com/charts/rap-song/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_song)

    def parse_song(self, response):
        liste_song = response.css('.o-chart-results-list-row-container')
        
        for song in liste_song:
            item = BillboardItem()
            
            #name
            try:
                item['name'] = response.css('div.chart-results h2::text')[0].extract().strip()
            except:
                item['name'] = 'None'
            
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
            
               # Dernière position au classement de la musique
            try:
                item['last_position'] = song.css('li.o-chart-results-list__item .c-label.a-font-primary-bold-l::text')[0].extract().strip()
            except:
                item['last_position'] = song.css('li.o-chart-results-list__item .c-label.a-font-primary-m::text')[0].extract().strip()
               
            # Meilleur position au classement de la musique
            try:
                item['peak_position'] = song.css('li.o-chart-results-list__item .c-label.a-font-primary-bold-l::text')[1].extract().strip()
            except:
                item['peak_position'] = song.css('li.o-chart-results-list__item .c-label.a-font-primary-m::text')[1].extract().strip()
                
            # Durée dans le classement
            try:
                item['weaks_on_charts'] = song.css('li.o-chart-results-list__item .c-label.a-font-primary-bold-l::text')[2].extract().strip()
            except:
                item['weaks_on_charts'] = song.css('li.o-chart-results-list__item .c-label.a-font-primary-m::text')[2].extract().strip()
        
            yield item