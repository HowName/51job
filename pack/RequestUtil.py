"""
user:long
"""
import requests


class RequestUtil(object):
    def __init__(self):
        pass

    def get(self, url):
        r = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        })
        r.encoding = 'GBK'
        status_code = r.status_code

        if status_code == 200:
            return r.text
        else:
            return ''
