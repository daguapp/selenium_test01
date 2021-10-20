import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
"""生成时间戳"""
timestamp=str(round(time.time()*1000)) #round（x[,n]） x：数值，n：保留n位小数
print(timestamp)

d=webdriver.Chrome()
d.switch_to.default_content()
