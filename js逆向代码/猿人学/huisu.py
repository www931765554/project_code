import requests
import execjs
import time
import json
if __name__ == '__main__':
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'match.yuanrenxue.com',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest'
    }
    with open('./回溯.js','r',encoding='utf-8') as f:
        a = f.read()
    # t = int(time.time() * 1000)
    m= execjs.compile(a).call('get_m_value')
    t = execjs.compile(a).call('times')
    sum3 = 0
    sum2 = 0
    sum1 = 0
    total_sum = 0
    for page in range(1,4):
        url = 'http://match.yuanrenxue.com/api/match/6'
        q = '1-'+str(t)+'|'
        params = {
            'page':page,
            'm':m,
            'q':q
        }
        res = requests.get(url, headers=header,params=params)
        data = json.loads(res.text)
        for datas in data['data']:
            sum3+=datas['value']
            sum2+=datas['value']*8
            sum1+=datas['value']*15
            total_sum+=datas['value']*24
    print(f'三等奖总数为:{sum3}元',)
    print(f'二等奖总数为:{sum2}元',)
    print(f'一等奖总数为:{sum1}元',)
    print(f'总金额总数为:{total_sum}元',)


