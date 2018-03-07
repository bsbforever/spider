__author__ = 'bsbfo'
#coding=utf8
import os
import re
#from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
if __name__=='__main__':
    #driver = selenium.webdriver.Chrome(r'C:\Users\bsbfo\Downloads\chromedriver.exe')
    driver = selenium.webdriver.Chrome()
    login_url='https://kyfw.12306.cn/otn/login/init'
    driver.get(login_url)
    time.sleep(2)
    username= driver.find_element_by_id('username')
    password= driver.find_element_by_id('password')
    username.clear()
    password.clear()
    username.send_keys("username")
    password.send_keys("password")
    while True:
        current_url = driver.current_url # driver.current_url代表driver当前页面url
        if current_url != login_url:
            if current_url[:-1] != login_url:  # choose wrong verify_pic
                print ('登陆成功，跳转中!')
                break
        else:
            time.sleep(5)
            print (u'等待用户图片验证')

    book_url='https://kyfw.12306.cn/otn/leftTicket/init'

    driver.get(book_url)

    # 选择出发地
    driver.find_element_by_id('fromStationText').click()
    fromStation= driver.find_element_by_xpath('//*[@id="ul_list1"]/li[2]')
    #fromStation =driver.find_element_by_id("fromStationText").sendkeys("沈阳");
    fromStation.click()

    #选择目的地
    driver.find_element_by_id('toStationText').click()
    ToStation= driver.find_element_by_xpath('//*[@id="ul_list1"]/li[13]')
    ToStation.click()

    #选择出发时间
    driver.find_element_by_id('train_date').click()
    train_date= driver.find_element_by_xpath('/html/body/div[30]/div[2]/div[2]/div[1]/div')
    train_date.click()



    #判断车票是否可订购

    #all_ticket = driver.find_element_by_id('queryLeftTable')
    #ticket=driver.find_element_by_xpath('//*[@id="ticket_5l0000D35271"]/td[13]/a')
    #ticket = all_ticket.find_element_by_xpath('//tr[1]/td[last()]')
    #count=0

    tickets=['D3094:5l000D3094601','G7024:51000d702454']
    bookable=0 #当车次可用时该值为1跳出循环
    while bookable==0:
        driver.find_element_by_id('query_ticket').click() #点击查询
        time.sleep(5)
        for i in tickets:
            path=i.split(':')[1]
            checi=i.split(':')[0]
            yd_path='//*[@id="ticket_'+path+'"]/td[13]/a'
            edz_path='//*[@id="ticket_'+path+'"]/td[4]'
            wz_path = '//*[@id="ticket_' + path + '"]/td[11]'
            print ('正在检测车次'+ checi)
            try:

                ticket = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, yd_path))
                )
                #print(edz)
                #print(wz)
                time.sleep(0.5)
                #获取二等座票数
                edz = driver.find_element_by_xpath(edz_path).text
                time.sleep(0.5)
                #获取无座票数
                wz = driver.find_element_by_xpath(wz_path).text

                #print (edz)
                #print(wz)
                if edz!='无'or wz!='无':
                    ticket.click() #点击预定
                    bookable=1
                    break

            except Exception as e:
                #count=count+1
                #print('车次'+checi+'目前不能预定，尝试第 '+ str(count) +' 次')
                print('车次' + checi + '目前不能预定，尝试下一车次')
                #continue
        print ('所有车次不可订购，刷新继续中..')


    confirm_url='https://kyfw.12306.cn/otn/confirmPassenger/initDc'

    while True:
        current_url = driver.current_url
        if current_url == confirm_url: #准备选座位
            try:
                passenger0 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'normalPassenger_0')) #获取第一名乘客
                )
                passenger0.click()
                driver.find_element_by_id('submitOrder_id').click()

                seat = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="id-seat-sel"]/div[2]/div[2]/ul[1]/li/a'))
                ) #选择靠窗位置
                seat.click()


                #确认订购
                buy_ticket = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'qr_submit_id'))
                )
                buy_ticket.click()
              #  print (driver.get_cookies())
            except Exception as e:
                print (e)
            finally:
                break
        else:
            time.sleep(5)
            print (u'等待跳转至确认页面')

    #driver.close()



    #print (all_ticket)
