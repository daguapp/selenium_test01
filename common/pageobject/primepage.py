from time import sleep
from selenium import webdriver
from common.baseobject.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PrimePage(BasePage):
    """选品方舟首页元素及功能流程"""
    prime_url="https://qbt.mobduos.com/#/dashboard"
    yesterday_sales=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[1]') #昨日大盘销售量
    yesterday_gmv=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[3]') #昨日大盘销售额
    brand_select=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div')#品牌行情下拉框
    brand_ranking=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div')#品牌销量排行榜
    sector_news=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[4]/div[1]/div/div[1]/ul/li[1]/a/img') #行业资讯链接
    elite_course=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[4]/div[1]/div/div[2]/ul/li[1]/a/span')#精选课程
    shift_pic=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[4]/div[2]/div/div/div/div/div/div/a/img')#轮播图
    brand_sales=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[4]/div[2]/div/div/div/div/div/div/a/img')#关注品牌销量
    shop_sales=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]')#关注店铺销量
    goods_sales=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]')#关注商品销量
    brand_gmv=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[5]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]')#关注品牌销售额
    yesterday=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[5]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/label[1]')#昨日数据
    recent_day=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[5]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/label[2]/span[2]') #近七天数据
    thirty_day=(By.XPATH,'//*[@id="ice-container"]/div/div[2]/div/div[5]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/label[3]/span[2]')

#点击
def click_yesterday_gmv(self,*args):
    self.click_ele(*args)



