# -*- coding:utf-8 -*-
from time import sleep
import pytest
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument(r"user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data")  # 把数据传入程序
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://qbt.mobduos.com/#/dashboard")
driver.find_element_by_xpath('//*[@id="ice-container"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div').click()
driver.switch_to.active_element.send_keys(Keys.DOWN)#定位不到的元素
driver.switch_to.active_element.send_keys(Keys.DOWN)
driver.switch_to.active_element.send_keys(Keys.ENTER)