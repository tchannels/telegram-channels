import json

from ChannelsScraper import ChannelsScraper            

if __name__ == "__main__":
    scraper = ChannelsScraper()
    scraper.wait()
    with open('channels.json', 'w') as outfile:
        json.dump(scraper.channel_names, outfile)
    # For now we just write channel names to file
    # TODO: get channel info by name
