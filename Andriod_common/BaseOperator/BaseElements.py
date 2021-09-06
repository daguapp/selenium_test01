from appium import webdriver
class BaseElement:
    """Appium连接手机参数设置"""
    server = r'http://localhost:4723/wd/hub' #Appium server服务
    desired_capabilities={
        'platformName': 'Android', #平台名称
        'driverName': '127.0.0.1:62001', #设备名称
        'platformVersion': '7.1.3', #系统版本号
        'appPackage': 'com.pengda.mobile.hhjz', #APP包名
        'appActivity': '.ui.login.activity.LoginActivity' #启动页
    }

    def __init__(self):
        self.driver=webdriver.Remote(self.server, self.desired_capabilities)
        self.driver.implicitly_wait(5)

    def locate_id(self,id):   #定位id
        try:
           return self.driver.find_element_by_id(id)
        except:
            print("找不到该元素:id=%s"%(id))

    def locate_xpath(self,xpath): #定位xpath
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            print("找不到该元素:xpath=%s" % (xpath))

    def locate_css(self,css): #定位css
        try:
            return self.driver.find_elements_by_css_selector(css)
        except:
            print("找不到该元素:css=%s" % (css))

    def locate_linktext(self,linktext): #定位linktext
        try:
            return self.driver.find_element_by_link_text(linktext)
        except:
            print("找不到该元素:linktext=%s" % (linktext))

    def locate_name(self,name): #定位name
        try:
            return self.driver.find_element_by_name(name)
        except:
            print("找不到该元素:name=%s" % (name))


