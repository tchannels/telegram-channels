import urllib.request
import threading
import time

from .ChannelsHTMLParser import ChannelsHTMLParser

class ChannelsScraper:
    """
        This class politely asks telegramchannels.me to share it's HTML 
        and gives all dirty work to ChannelsHTMLParser.
        Feel free to ask how it's going using method wait()
    """
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        self.channel_names = []
        url = 'https://telegramchannels.me/channels?page={page}'
        self.threads = []
        for i in range(1, 21):
            thread = threading.Thread(target=self.fetch_url, args=(url.format(page=i), ))
            thread.start()
            self.threads.append(thread)
    
    def fetch_url(self, url):
        request = urllib.request.Request(url, headers=self.headers, method='GET')
        url_data = urllib.request.urlopen(request)
        parser = ChannelsHTMLParser()
        parser.feed(str(url_data.read()))
        self.channel_names += parser.channel_names
        
    def wait(self):
        start_time = time.time()
        while True:
            active_threads = sum([1 for thread in self.threads if thread.isAlive()])
            time_elapsed = time.time() - start_time
            print('Current number of active threads is %s. Time elapsed is %s seconds' 
                % (active_threads, time_elapsed))

            if active_threads == 0:
                break

            time.sleep(1)
