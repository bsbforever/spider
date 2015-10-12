__author__ = '42274'
#coding utf-8
from lxml import html
import time
import requests
import os
import random
#download_link={}
#movieurl='http://www.baidu.com'
USER_AGENTS = [
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
  "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
  "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
  "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
  "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]


proxies = {
  "http": "http://27.191.147.166:9999",
}



def getdownloadaddress(download_title,page,USER_AGENTS,prefix):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               "Cache-Control": "max-age=0",
               'Connection':'keep-alive',
               'Host':'www.xixihd.com',
               'User-Agent':USER_AGENTS[random.randint(0,len(USER_AGENTS))-1]}
    time.sleep(2)
    r = requests.get(page,headers=headers)

    r.encoding=r.apparent_encoding
    tree=html.fromstring(r.text)
    dlink=tree.xpath('//a[@class=\'d_button\']/@href')[0]
    downlink=prefix+dlink
    download_torrent(download_title,downlink)
    #print (download_link)



def download_torrent(download_title,downlink):
    directory=download_title.split(' ')[0]

    directory=directory.replace(':','')

    directory=directory.replace('/','')

    directory=directory.replace('?','')

    directory='g:\\Xixi1\\'+directory
    download_title=download_title.replace('/','')
    download_title=download_title.replace('?','')
    fname=directory+'\\'+download_title+'.torrent'
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               "Cache-Control": "max-age=0",
               'Connection':'keep-alive',
               'Host':'www.xixihd.com',
               'User-Agent':USER_AGENTS[random.randint(0,len(USER_AGENTS))-1]}
   # print(directory)
    #print(fname)
    #time.sleep(10000)
    if os.path.exists(directory):
        if os.path.exists(fname):
            print ('File '+fname+' is already exists,SKIP......')
        else:
            print ('Folder is already exists,Downloding '+fname+'.....Please Waiting')
            time.sleep(2)
            r=requests.get(downlink,headers=headers)
            with open (fname,"wb") as code:
                code.write(r.content)
            print('Download Compelte')
    else:
        os.mkdir(directory)
        print ('Downloding '+fname+'.....Please Waiting')
        time.sleep(2)
        r=requests.get(downlink,headers=headers)
        with open (fname,"wb") as code:
            code.write(r.content)
        print('Download Compelte')
def getmovielink(movieurl,prefix,USER_AGENTS):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               "Cache-Control": "max-age=0",
               'Connection':'keep-alive',
               'Host':'www.xixihd.com',
               'User-Agent':USER_AGENTS[random.randint(0,len(USER_AGENTS))-1]}
  #  s = requests.Session()


    download={}
    prefix_link=[]
    r = requests.get(movieurl,headers=headers)
    r.encoding=r.apparent_encoding

    tree=html.fromstring(r.text)
    title=tree.xpath('//ul[@id="new_ul"]/li/div/a/@title')
    link=tree.xpath('//ul[@id="new_ul"]/li/div/a[@title]/@href')
    for i in link:
        prefix_link.append(prefix+i)
    for i in range(0,len(title)):
        download[title[i]]=prefix_link[i]
  #  for keys in download:
   #     print (keys,download[keys])

    return download
#j=0

prefix='http://www.xixihd.com'
for i in range(1,5):

    movieurl='http://www.xixihd.com/?mod=list&id=1&form=0&movie_type=0&year=0&country=0&page='+str(i)
    print('\033[1;32;40m Now Downloading Page '+str(i)+'............\033[0m')


    download=getmovielink(movieurl,prefix,USER_AGENTS)




    for keys in download:
        download_title=keys
        page=download[download_title]

       # print (download_title,page)
        getdownloadaddress(download_title,page,USER_AGENTS,prefix)
        time.sleep(2)
