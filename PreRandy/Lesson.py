#coding:utf-8
import requests,time,re
from PIL import Image
from urllib.parse import unquote
from bs4 import BeautifulSoup

def url_decode(url):
    result = unquote(url)
    datas = result
    dict_datas = {}
    datas=datas.split("&")
    for data in datas:
        i,y=data.split('=')
        if y:
            dict_datas[i]=y
    return dict_datas

session = requests.session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
user = input('请输入用户名：')
passwd = input('请输入密码：')
# user = 80170905
# passwd = 80170905

code = session.get('http://flwm.bcpl.cn/verifycode/index')

a = str(int(time.time()))+'code.jpg'
with open(a,'ab')as f:
    f.write(code.content)

im = Image.open(a)
im.show()

index_data = url_decode('visits_type=1&visits_productid=1&visits_first=0&rnum={0}'.format(str(time.time()/10000000000)))
index = session.post(url='http://flwm.bcpl.cn/tongji/visits/index',data=index_data,headers=headers)

in_code = input('请输入图片上验证码：')
login_data = {
    'username': user,
    'password': passwd,
    'verifycode': in_code
}
login_data['verifycode'] = str(in_code)
login_url = 'http://flwm.bcpl.cn/login/loginokajx'

login = session.post(login_url,headers = headers,data=login_data)

if "success" in login.text:
    print(("账号：%s，登录成功!\n"%login_data['username']))
else:
    print((login.text))

select = session.get('http://flwm.bcpl.cn/member/home/default')
print('正在查询我的课程...')
soup_s = BeautifulSoup(select.text,'lxml')
href_s = soup_s.find_all('div',class_="me-2")
list_h = {}
list_t = {}
for i in href_s:
    data_s = i.find('a',href=re.compile(r'^(/portal)'))
    title = data_s.get_text().strip()
    href = 'http://flwm.bcpl.cn' + data_s['href'].strip()
    print((href_s.index(i)+1,'.'+title))
    list_h[str(href_s.index(i))] = href
    list_t[str(href_s.index(i))] = title


url = int(input('\n请输入课程编号：'))
check = session.get(list_h[str(url-1)])
print(('正在解析课程：%s'%list_t[str(url-1)]))
soup = BeautifulSoup(check.text,'lxml')
hrefs = soup.find_all('div', class_=['xxo_zhishi','renwu_fj'])
text = ''
for a in hrefs:
    text += str(a)
new_hrefs = BeautifulSoup(text,'lxml').find_all('a')
for li in new_hrefs:
    title = li.get_text().strip()
    href = 'http://flwm.bcpl.cn' + li['href'].strip()
    print(('正在浏览：%s\t%s'%(href,title)))
    check = session.get(href)
    time.sleep(1)