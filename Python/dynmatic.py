from appium import webdriver
import os
import re
class Dynmatics:

    """Appium连接手机参数设置"""
    server = r'http://localhost:4723/wd/hub' #Appium server服务
    desired_capabilities={
        'platformName': 'Android', #平台名称
        'driverName': '127.0.0.1:62001', #设备名称
        'platformVersion': '7.1.3', #系统版本号
        'appPackage': 'com.pengda.mobile.hhjz', #APP包名
        'appActivity': '.ui.login.activity.LoginActivity'#启动
    }

    def get_mobile_id(self):
        devices=[]
        response=os.popen("adb devices")
        text=response.read()
        s=text.split("\n")
        result=[x for x in s[1:] if x != ""]
        for x in result:
            y=x.split("\tdevice")
            # y=re.split("\tdevice",x)
            for j in y:
                j.strip()
                if j !="":
                    devices.append(j)
        return devices #返回设备列表

if __name__ == '__main__':
    Dynmatics().get_mobile_id()
import re
a='Beautiful, is; better*than\nugly'
# 四个分隔符为：,  ;  *  \n
