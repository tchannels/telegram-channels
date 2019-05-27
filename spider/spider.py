"""
TODO: с любого списка телеграм каналов парсить ссылки на канал и идентификаторы для t.me
"""
from scrapy import spiders

class MrSpider(spiders.CrawlSpider):
    name = "MrSpider"
    allowed_domains = ['tlgrm.eu']
    start_urls = ['https://tlgrm.eu/channels']
    
    def parse(self, response):
        pass