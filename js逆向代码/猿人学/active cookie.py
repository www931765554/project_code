import requests
import re
import json
from collections import Counter
class Three:
    def __init__(self):
        self.t = {
            "Host": "match.yuanrenxue.com",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "User-Agent": "yuanrenxue.project",
            "Accept": "*/*",
            "Origin": "http://match.yuanrenxue.com",
            "Referer": "http://match.yuanrenxue.com/match/3",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.session = requests.session()
        self.data_lists = []
    def parse(self,ul,page):
        for i in range(1,int(page)+1):
            res1 = self.session.post(url=ul)
            sessionid = res1.headers['Set-Cookie'][:res1.headers['Set-Cookie'].find(';')]
            self.session.headers['Cookie'] = sessionid
            url2 = 'http://match.yuanrenxue.com/api/match/3?page={}'.format(i)
            res2 = self.session.get(url2)
            data = json.loads(res2.text)['data']
            for _, values in enumerate(data):
                self.data_lists.append(values['value'])
        return self.data_lists
    def run(self):
        u1 = 'http://match.yuanrenxue.com/logo'
        self.session.headers = self.t
        parse_list = self.parse(u1,5)
        print(Counter(parse_list))
if __name__ == '__main__':
    spider = Three()
    spider.run()

