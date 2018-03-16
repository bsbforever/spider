__author__ = 'bsbfo'
#coding=utf8
import requests
import json
from bs4 import BeautifulSoup
import json

def login_51cto():
    s=requests.Session()
    #login_url = 'http://home.51cto.com/index'
    login_url='http://home.51cto.com/index'
    content=s.get('http://home.51cto.com/home').content
    #获取csrf token
    soup = BeautifulSoup(content,"lxml")
    token=soup.find('meta',attrs = {'name' : 'csrf-token'})['content']
    #print (token)
    header={
    'Connection': 'keep-alive',
        'Host': 'home.51cto.com',
        'Origin': 'http://home.51cto.com',
        'Referer':'http://home.51cto.com/index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    data={
        '_csrf':token,
        'LoginForm[username]':'bsbforever',
   'LoginForm[password]': '296701298a',
    'LoginForm[rememberMe]': '0',
    'login-button': '登 录'
    }

    #模拟POST 51cto 登陆

    s.post(url=login_url,headers=header,data=data)
    #print (result.url)

    # 利用保持的Session打开主页获取登录信息
    result=s.get('http://home.51cto.com/home').text
    if 'bsbforever' in result:
        print ('恭喜,登陆51cto成功,领取下载豆中..')


    #利用保持的Session领取下载豆
    download=s.post('http://down.51cto.com/download.php?do=getfreecredits&t=0.8367867217711695').text


    if '2' in download.split(',')[1]:
        print ('领取成功,当前下载豆:'+ download.split(',')[0])
    elif '1' in download.split(',')[0]:
        print (download)
        print ('抱歉,今天已经领取,请明天再来,当前下载豆:'+download.split(',')[1])
    else:
        print ('请注意,领取失败')
    #print (download)


def login_wodehd():
    s=requests.Session()
    login_url='https://www.wodehd.com/?user=login'
    content=s.get('https://www.wodehd.com/?user=login',verify=False).content
    # 获取echostr
    soup = BeautifulSoup(content,"lxml")
    echostr=soup.find('input',attrs = {'name' : 'echostr'})['value']
    #print (echostr)
    #print (token)
    header={
    'Connection': 'keep-alive',
        'Host': 'www.wodehd.com',
        'Origin': 'https://www.wodehd.com',
        'Referer':'https://www.wodehd.com/?user=login&reurl=https://www.wodehd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    data={
        'echostr':echostr,
        'reurl':'https://www.wodehd.com/',
   'popup': 'false',
    'iframe': '',
    'username': 'bsbforever',
    'password': '296701298a'
    }

    #模拟POST 51cto 登陆

    r=s.post(url=login_url,headers=header,data=data)
    #print (result.url)
    #print (r.text)
    # 利用保持的Session打开主页获取登录信息
    result=s.get('https://www.wodehd.com/').text
    #print (result)
    if 'bsbforever' in result:
        print ('登陆成功')

    #movie=s.get('https://www.wodehd.com/imdb-19893.html').content
    #soup = BeautifulSoup(movie,"lxml")
    #print (soup)
    movie_link=[]
    #movie_link=soup.find_all('a',attrs = {'class' : 'filetitle'})
    #for i in movie_link:
     #   print (i)
    movie_page=s.get('https://www.wodehd.com/content-56797.html').content
    soup = BeautifulSoup(movie_page,"lxml")
    movie_title=soup.find('a',attrs = {'class' : 'filetitle'}).text
    movie_link='https://www.wodehd.com'+soup.find('a',attrs = {'class' : 'filetitle'})['href']
    print(movie_link)
    print(movie_title)
if __name__=="__main__":
    login_51cto()
    #login_wodehd()
