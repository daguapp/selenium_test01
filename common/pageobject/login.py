from time import sleep
from selenium import webdriver
from common.baseobject.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """定位页面元素和操作步骤"""
     #项目地址url
    test_url="http://150.158.219.67/#/login"

    #输入账号和密码
    username_loc=(By.ID,"username")
    password_loc=(By.ID,"password")

    #点击登录按钮
    login_loc=(By.ID,"TencentCaptchaBtn")

    #滑块按钮
    slider_iframe=(By.ID,"tcaptcha_iframe")
    slider_button=(By.ID,"tcaptcha_drag_thumb")

    #登录选品方舟
    def test_login(self,name="18582339746@mobduos",word="18582339746"):
        self.get_url(self.test_url)
        sleep(2)
        self.input_key(*self.username_loc,name)
        sleep(2)
        self.input_key(*self.password_loc,word)
        sleep(2)
        self.click_ele(*self.login_loc)
        sleep(3)
        #定位并跳转到滑块所在的iframe
        iframe = self.driver.find_element(*self.slider_iframe)
        self.driver.switch_to.frame(iframe)
        local = self.driver.find_element(*self.slider_button)
        #实例化鼠标操作对象
        action = ActionChains(self.driver)
        #鼠标移动到滑块按钮
        action.click_and_hold(local).perform()
        #移动滑块按钮至缺口位置
        action.move_by_offset(222, 0).perform()
        #移动到缺口后再次点击滑块按钮验证
        self.click_ele(*self.slider_button)


if __name__ == '__main__':
    lp=LoginPage(webdriver.Chrome())
    lp.test_login()
