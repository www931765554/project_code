import execjs
import requests
class Active_Cookieone:
    def __init__(self):
        self.headers = {
		"Accept":"application/json,text/javascript,*/*;q=0.01",
		"Accept-Encoding":"gzip,deflate",
		"Accept-Language":"zh-CN,zh;q=0.9",
		"Cache-Control":"no-cache",
		"Connection":"keep-alive",
		"Host":"match.yuanrenxue.com",
		"Pragma":"no-cache",
		"Referer":"http://match.yuanrenxue.com/match/2",
		"User-Agent":"yuanrenxue.project",
		"X-Requested-With":"XMLHttpRequest",
    }
        self.urls = 'http://match.yuanrenxue.com/api/match/2'
    def read_cookie(self):
        with open('./get_active_cookie.js','r',encoding='utf-8') as file:
            content = file.read()
        target_cookie = execjs.compile(content).call('get_value')
        return 'm='+target_cookie
    def run(self):
        self.headers['Cookie'] = self.read_cookie()
        sum = 0
        for i in range(1,6):
            params = {
                'page':str(i)
            }
            res = requests.get(url=self.urls,headers=self.headers,params=params)
            for keys in res.json()['data']:
                sum+=keys['value']
        print(f'总数为：{sum}')
if __name__ == '__main__':
    Active_Cookieone().run()