from selenium import webdriver
# import logging
from selenium.webdriver.support.ui import  WebDriverWait
# #日志消息级别DEBUG<INFO<WARNING<ERROR<CRITICAL
#
# my_logger=logging.Logger("my_logger") #创建一个Logger日志记录器对象
#
# myhanlder=logging.FileHandler("log.txt") #定义handler日志处理器（决定日志存储位置）
#
# myhanlder.setLevel(logging.INFO) #设置日志的级别（level）和输出的格式Formatters（日志格式器）
# my_format=logging.Formatter("时间：%(asctime)s 日志信息：%(message)s 行号：%(lineno)d")
#
# myhanlder.setFormatter(my_format)  #把handler添加到对应的logger中
# my_logger.addHandler(myhanlder)
# #使用
# my_logger.info("这是测试日志")

class Test:

    def __init__(self,name):
        self.name=name
        print("这是名字：%s"%(name))



    def test01(self,age):
        print("%s的年龄：%s"%(self.name,age))

    def teardown_class(self):
        print("这是teardownclass方法")

t=Test("小明")
t.test01(14)