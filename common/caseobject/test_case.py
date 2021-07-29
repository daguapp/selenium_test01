from time import sleep
import allure
import pytest
import os
from ddt import ddt,data,unpack,file_data
from selenium import webdriver
from common.baseobject.base import BasePage
from common.read_excel.excel import read_xls
from common.pageobject.shop_analayse import ShopAnalayse
from common.pageobject.brand_analayse import  BrandPage
from common.pageobject.login import LoginPage
#导入写好的各页面元素定位及操作流程模块
class TestFangZhou:

    #打开浏览器
    def setup(self)->None:
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument(r"user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data")  # 把数据传入程序
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
        self.driver = webdriver.Chrome(options=chromeOptions)

    def teardown(self)->None:
        sleep(1)
        self.driver.close()

    """利用excel导入登录模块测试用例"""
    #pytest装饰器，前者参数是字符串，对应函数中的参数，后者对应一个数据集合
    #相当于ddt数据驱动
    # @pytest.mark.parametrize("case",read_xls("../Data/case.xlsx",sheet_name="Sheet1"))
    # def test_01_login(self,case):
    #     xh, case_title, username, password, is_exc, result, bz = case
    #     lg=LoginPage(self.driver)
    #     return lg.test_login(username,password)

    #
    # def test_02_brand_analyse(self):
    #     bs=BrandPage(self.driver
    #     bs.brand_search()
    @pytest.mark.test
    @pytest.mark.parametrize("name",[(257738004,"李宁泰海专卖店"),(394291029,"沃尔普大家电专营店"),(181454546,"晨光正强专卖店"),(17212121,"测试店铺")])
    def test_03_shop_search(self,name):
        """店铺搜索功能"""
        shop_id,shop_name=name
        ss=ShopAnalayse(self.driver)
        ss.click_shop_analayse_btn(shop_id=shop_id,shop_name=shop_name)
if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp -o ./report --clean exit 0")

#pytest [测试文件] -s -q --alluredir=./result --clean-alluredir

#--alluredir这个选项，用于指定存储测试结果的路径
#--clean-alluredir 这个选项用来清除之前生成的结果



