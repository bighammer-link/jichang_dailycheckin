import requests, json,re

SCKEY = os.environ.get('SCKEY')


# 这是获取登录https://fenda.cloud/user后的cookie
cookie = os.environ.get('COOKIE')


url_info = 'https://fenda.cloud/user/profile'
url = 'https://fenda.cloud/user/checkin'
headers = {
    'cookie': f'{cookie}',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

html_info = requests.get(url=url_info, headers=headers).text
html = requests.post(url=url, headers=headers)
result = json.loads(html.text)['msg']
info = "".join(re.findall('<span class="user-name text-bold-600">(.*?)</span>', html_info, re.S))  # 获取账户名称
content=info+'\n'+result
print(content)
# 这是server酱的推送方式：https://sct.ftqq.com/
requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY,"fenda签到",content))
