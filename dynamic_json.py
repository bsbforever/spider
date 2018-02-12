__author__ = 'bsbfo'
#coding=utf8
import requests
import json
def douban_tv():
    tv_list=[]
    url='https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    r = requests.get(url,verify=False)
    content=r.text
    result=json.loads(content) # https://jsonformatter.curiousconcept.com/

    tvs=result['subjects']

    for i in range (0,len(tvs)):
        tv={}
        tv['rate']=tvs[i]['rate']
        tv['cover']=tvs[i]['cover']
        tv['url']=tvs[i]['url']
        tv['title']=tvs[i]['title']
        tv_list.append(tv)
    return tv_list


def douban_movie():
    tv_list=[]
    url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=100&page_start=0'
    r = requests.get(url,verify=False)
    content=r.content
    result=json.loads(content) # https://jsonformatter.curiousconcept.com/

    tvs=result['subjects']

    for i in range (0,len(tvs)):
        tv={}
        tv['rate']=tvs[i]['rate']
        tv['cover']=tvs[i]['cover']
        tv['url']=tvs[i]['url']
        tv['title']=tvs[i]['title']
        tv_list.append(tv)
    return tv_list

if __name__=="__main__":
    result=douban_movie()
    for i in result:
        print (i)
