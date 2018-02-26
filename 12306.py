__author__ = 'bsbfo'
#coding=utf8
import os
#from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
if __name__=='__main__':
    driver = selenium.webdriver.Chrome(r'C:\Users\bsbfo\Downloads\chromedriver.exe')
    login_url='https://kyfw.12306.cn/otn/login/init'
    driver.get(login_url)
    #time.sleep(10)
    username= driver.find_element_by_id('username')
    password= driver.find_element_by_id('password')
    username.clear()
    password.clear()
    username.send_keys("ezio_shi")
    password.send_keys("296701298")
    while True:
        current_url = driver.current_url
        if current_url != login_url:
            if current_url[:-1] != login_url:  # choose wrong verify_pic
                print ('Login finished!')
                break
        else:
            time.sleep(5)
            print (u'------------>等待用户图片验证')

    book_url='https://kyfw.12306.cn/otn/leftTicket/init'

    driver.get(book_url)

    driver.find_element_by_id('fromStationText').click()
    fromStation= driver.find_element_by_xpath('//*[@id="ul_list1"]/li[10]')
    fromStation.click()
    driver.find_element_by_id('toStationText').click()
    ToStation= driver.find_element_by_xpath('//*[@id="ul_list1"]/li[13]')
    ToStation.click()

    driver.find_element_by_id('train_date').click()
    train_date= driver.find_element_by_xpath('/html/body/div[30]/div[2]/div[2]/div[2]/div')
    train_date.click()

    driver.find_element_by_id('query_ticket').click()
