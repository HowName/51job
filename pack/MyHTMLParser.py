"""
user:long
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    cur_stag = None
    price = 0
    img = ''
    desc = ''

    def handle_starttag(self, tag, attrs):
        print("start tag:", tag)
        self.cur_stag = tag

        if (tag == 'img'):
            self.img = attrs[1][1]

        pass

    def handle_data(self, data):
        data = data.strip()
        print("data  :", data)
        self.desc += data

        if (self.cur_stag == 'em'):
            self.cur_stag = ''
            self.price = data
        pass

    def handle_endtag(self, tag):
        print("end tag :", tag)
        pass

    def handle_startendtag(self, tag, attrs):
        print("startend tag :", tag)
        pass

    def error(self, message):
        print(message)

    def get_parse(self):
        return {'img': self.img, 'price': self.price, 'desc': self.desc}
