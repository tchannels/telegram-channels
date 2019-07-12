import scrapy
import logging
from .DBManager import DBManager

logger = logging.getLogger('channels_crawler')

class Spider(scrapy.Spider):
    def __init__(self):
        self.name = 'MrSpider'
        self.custom_settings = {
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        self._db_manager = DBManager()
        super().__init__()
        logger.debug('Spider initialized')

    def start_requests(self):
        for page in range(1, 21):
            yield scrapy.Request('https://telegramchannels.me/channels?page=%d' % page, callback=self.get_channels_data)

    def get_channels_data(self, response):
        channels = Spider.parse_channel_names(response)
        for channel in channels:
            yield scrapy.Request('https://t.me/%s' % channel, callback=self.get_channel_info)

    def get_channel_info(self, response):
        data = {
            'channel_id': response.url.split('/')[-1],
            'title': response.xpath('//meta[@property="og:title"]/@content')[0].extract(),
            'image': response.xpath('//meta[@property="og:image"]/@content')[0].extract(),
            'description': response.xpath('//meta[@property="og:description"]/@content')[0].extract()
        }
        self._db_manager.save_channel(data)
            
    @staticmethod
    def parse_channel_names(response):
        channels = []
        for link in response.xpath('//a[contains(@href, "/channels/")]/@href').extract():
            channels.append(link.split('/')[-1])
        
        return channels
