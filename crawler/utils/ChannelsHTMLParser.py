from html.parser import HTMLParser

class ChannelsHTMLParser(HTMLParser):
    """
        It's just a good guy that will find all channel names from HTML 
        that you gave him and store it to channel_names variable.
    """
    channel_names = []
    def handle_starttag(self, tag, attrs):
        channel_link_prefix = 'https://telegramchannels.me/channels/'
        if tag != 'a':
            return
        
        for name, value in attrs:
            if name == 'href' and value and value.startswith(channel_link_prefix):
                self.channel_names.append(value[len(channel_link_prefix):])
