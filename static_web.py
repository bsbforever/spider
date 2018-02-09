__author__ = 'bsbfo'
#coding=utf8
import requests
from bs4 import BeautifulSoup
def douyu(douyugame):
    game_list=[]
    url='HTTPs://www.douyu.com/directory/game/'+douyugame
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'data-cid' : True})
    for i in live_list:
        #print (i)
        try:
            all_game=i.find('a')
            #print (all_game)
            game_count=all_game.find('span',attrs = {'class' : 'dy-num fr'}).text
            #print (game_count)
            if '万' in game_count:
                game_count=float(game_count[0:-1])*10000

            if float(game_count)>8000:
                game_link='https://www.douyu.com'+all_game['href']
                #game_title=all_game['title'].encode('utf-8').decode('utf-8')
                game_title=all_game['title']
                game_picture= all_game.find('img')['data-original']
                game_nickname=all_game.find('span',attrs = {'class' : 'dy-name ellipsis fl'}).text
              #  print all_game
               # print game_link
                #print (game_title)
                #print game_picture
                #print game_nickname
                #print game_count
                #print '\n'
                #break
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)

        except Exception as e:
            print (e)
    return game_list


if __name__=="__main__":
    douyugame='lol'
    result=douyu(douyugame)
    for i in result:
        try:
           print (i)
        except Exception as e:
            print (e)
