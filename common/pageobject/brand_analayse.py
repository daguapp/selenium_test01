from time import sleep
from selenium import webdriver
from common.baseobject.base import BasePage
from selenium.webdriver.common.by import By

class BrandPage(BasePage):
    """定位品牌分析页面元素和操作流程"""

    brand_button=(By.LINK_TEXT,"品牌分析") #品牌搜索的元素定位
    search_input=(By.XPATH,"//input[@class=‘ant-input’ and @maxlength=‘32’]") #品牌搜索输入框
    search_button=(By.XPATH,"//button[@class='ant-btn ant-btn-primary']/i[@class='anticon anticon-search']") #查询按钮
    brand_url="https://qbt.mobduos.com/#/brand"
    #品牌搜索的操作流程
    def brand_search(self,content="立白"):
        self.get_url(self.brand_url)
        self.click_ele(self.brand_button)
        sleep(2)
        self.input_key(self.search_input,content)
        sleep(2)
        self.click_ele(self.search_button)


lista=[2,5,1,9,0,4,3]
for i in range(1,len(lista)):
    for x in range(0,len(lista)-i):
        if lista[x]>lista[x+1]:
            lista[x],lista[x+1]=lista[x+1],lista[x]
        else:
            pass
print(lista)