import requests, json,re



#这里是cookie
cookie ='uid=18609; email=wm3225579752%40outlook.com; key=4e44d97149d12434518c58c089b1bf45ba73540de437d; ip=a9cf7b85bd220d7eb3311336d7bab74b; expire_in=1674300595'

url_info = 'https://fenda.cloud/user/profile'
url = 'https://fenda.cloud/user/checkin'
headers = {
    'cookie': f'{cookie}',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
html_info = requests.get(url=url_info, headers=headers).text
html = requests.post(url=url, headers=headers)
result = json.loads(html.text)['msg']
info = "".join(re.findall('<span class="user-name text-bold-600">(.*?)</span>', html_info, re.S))
content=info+'\n'+result
print(content)

requests.post("https://sctapi.ftqq.com/SCT180477TOZkGM0Zqetd8Oyy4Y6QPp37J.send?title={}&desp={}".format("fenda签到",content))
