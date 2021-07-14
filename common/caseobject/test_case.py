from time import sleep
import pytest
import os
from selenium import webdriver
from common.baseobject.base import BasePage
from common.read_excel.excel import read_xls
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
    @pytest.mark.parametrize("case",read_xls("../Data/case.xlsx",sheet_name="Sheet1"))
    def test_01_login(self,case):
        xh, case_title, username, password, is_exc, result, bz = case
        lg=LoginPage(self.driver)
        return lg.test_login(username,password)

    def test_02_brand_analyse(self):
        bs=BrandPage(self.driver)
        bs.brand_search()
if __name__ == '__main__':
    pytest.main([r"pytest -v \test_case.py::TestFangZhou::test_02_brand_analyse"])



