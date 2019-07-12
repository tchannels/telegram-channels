import json
import logging
from scrapy.crawler import CrawlerProcess

from utils.MrSpider import Spider

if __name__ == "__main__":
    logger = logging.getLogger('channels_crawler')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('crawler.log')
    stream_handler = logging.StreamHandler()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.debug('Script initialized')
    process = CrawlerProcess()
    process.crawl(Spider)
    process.start()
