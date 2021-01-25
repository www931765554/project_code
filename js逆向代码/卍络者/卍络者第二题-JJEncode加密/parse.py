import requests
import execjs
import time
class JJEncode_project_parse:
    def __init__(self):
        self.header = {
		"Accept":"application/json,text/javascript,*/*;q=0.01",
		"Accept-Encoding":"gzip,deflate",
		"Accept-Language":"zh-CN,zh;q=0.9",
		"Cache-Control":"no-cache",
		"Connection":"keep-alive",
		"Content-Length":"67",
		"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
		"Cookie":"session=c2fd97cc-6298-4c9b-b381-b25192c14097.4vyZApj_c5NfL7g_nYvenNbFo34;__guid=170017250.164682424875080800.1611363477127.7908;monitor_count=34",
		"Host":"spider.wangluozhe.com",
		"Origin":"http://spider.wangluozhe.com",
		"Pragma":"no-cache",
		"Referer":"http://spider.wangluozhe.com/challenge/2",
		"User-Agent":"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.108Safari/537.36",
		"X-Requested-With":"XMLHttpRequest",
}
        self.session = requests.Session()
    def read_js_content(self):
        with open('./卍络者第二题-JJEncode加密.js','r',encoding='utf-8') as file:
            content = file.read()
        return content
    def run(self):
        url = 'http://spider.wangluozhe.com/challenge/api/2'
        sum = 0
        count = 0
        for i in range(1,101):
            _signature = execjs.compile(self.read_js_content()).call('get_sign')
            form_data = {
                'page':str(i),
                'count':'10',
                '_signature':_signature
            }
            data_cotent = None
            res = self.session.post(url,data=form_data,headers=self.header)
            if 'data' in res.json().keys():
                for datas in res.json()['data']:
                    sum+=datas['value']
                    count+=1
            else:
                count+=1
        print(f'获取记录数量为{count},总数为：{sum}')
        return sum
    def post_answeri(self):
        url = 'http://spider.wangluozhe.com/challenge/answer'
        form_data1 = {
            'id': '2',
            'answer': sum
        }
        res1 = self.session.post(url, headers=self.header, data=form_data1)
        print(res1.content.decode())
if __name__ == '__main__':
    Object = JJEncode_project_parse()
    Object.run()