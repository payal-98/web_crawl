import scrapy
from ..items import CrawlingItem

class CelebritySpide(scrapy.Spider):
    name='celebrity'
    start_urls = ['https://in.bookmyshow.com/person'

]

    def parse(self,response):
    
        items=CrawlingItem()
        artist=response.css('div.artist-block')
        inn=artist.css('.inner-block')
        img=inn.css('div.__img a').xpath("@href").extract()
        
        det=inn.css('.detail')
        #for det in inn:
        name=det.css('.__art-name::text').extract()
        items['name']=name
        items['img']=img
        yield items
        