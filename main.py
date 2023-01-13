import requests, json,re



#这里是cookie
cookie ='uid=18609; email=wm3225579752%40outlook.com; key=beae8f20751f7102ffefdc9cce4877d505bd35c527db4; ip=533c663251d318d9d1df3f7a5cfb416f; expire_in=1673682858'

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
