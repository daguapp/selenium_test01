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
        return self.driver.get(url)

    #定位元素
    def locate_element(self,*args):
        return self.driver.find_element(*args)

    #获取元素文本
    def locate_element_text(self,*args):
        return self.locate_element(*args).text #复用定位方法加上获取文本方法

    #点击事件
    def click_ele(self,*args):
        return self.locate_element(*args).click()#复用定位方法加上点击方法

    #清空所有值
    def clear_keys(self,*args):
        return self.locate_element(*args).clear() #复用定位方法加上点击方法
    #输入值
    def input_key(self,*args,keys):
        return self.locate_element(*args).send_keys(keys)#复用定位方法加上输入方法

    #执行js操作
    def execute_js(self,*args,js):
        return self.locate_element(*args).execute_script(js)
    #隐式等待
    def implicit_(self):
        return self.driver.implicitly_wait(10)

    #鼠标悬停事件
    def move_to_ele(self,*args):
        return ActionChains(self.driver).move_to_element(self.locate_element(*args)).perform()#创建一个Action对象，定位复用定位方法

    #切换iframe
    def switch_iframe(self,iframe_id):
        return self.driver.switch_to.iframe(iframe_id)

    #浏览器最大化
    def max_windows(self):
        return self.driver.maximize_window()

    #刷新当前页面
    def refresh_page(self):
        return self.driver.refresh()

    #当前页面截图
    def shot_screen(self,path):
        return self.driver.get_screenshot_as_file(path)

    #获取登录的cookie值
    def get_cookies(self):
        self.driver.get_cookies()

