from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
#基础层#封装selenium的基础方法，例如：打开URL，点击事件，输入事件

class BasePage:

    #构造函数传入一个driver变量
    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    #根据url打开页面
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def locate_element(self,*args):
        return self.driver.find_element(*args)
    #获取元素文本
    def locate_element_text(self,*args):
        return self.driver.find_element(*args).text

    #点击事件
    def click_ele(self,way,loc):
        return self.driver.find_element(way,loc).click()

    #输入值
    def input_key(self,way,loc,content):
        return self.driver.find_element(way,loc).send_keys(content)

    #鼠标移动事件
    def move_ele(self,way,loc):
        ActionChains(self.driver).move_to_element(self.driver.find_element(way,loc))


    #获取登录的cookie值
    def get_cookies(self):
        self.driver.get_cookies()

