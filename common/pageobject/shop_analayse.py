import time

from common.baseobject.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class ShopAnalayse(BasePage):
    """店铺分析模块元素和基础操作流程"""

    shop_analayse_btn=(By.LINK_TEXT,'店铺分析')
    shop_search_input=(By.XPATH,'//input[@class="ant-input" and @placeholder="请输入店铺ID或名称"] ')
    shop_search_btn=(By.XPATH,'//*[@id="content"]/div[2]/div[1]/div[2]/button')
    shop_detail_btn=(By.XPATH,'//*[@id="content"]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[1]/div/div[2]/div/a')
    shop_detail_cancel_btn=(By.XPATH,'//*[@id="content"]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[6]/button')

    def click_shop_analayse_btn(self,shopname):
        self.get_url("https://qbt.mobduos.com/#/dashboard")
        self.click_ele(*self.shop_analayse_btn)
        self.implicit_()
        self.input_key(*self.shop_search_input,keys=shopname)
        self.click_ele(*self.shop_search_btn)
        try:
            shop_detail_cancel_btn =self.locate_element(*self.shop_detail_cancel_btn).click()
            print("%s已找到该商品"%(shopname))

        except:
            print("%s不存在"%(shopname))