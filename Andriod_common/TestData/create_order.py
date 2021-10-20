from appium import webdriver
import time
class GetOrder:
    server = r'http://localhost:4723/wd/hub'  # Appium server服务
    desired_capabilities = {
        'platformName': 'Android',  # 平台名称
        'driverName': '127.0.0.1:62001',  # 设备名称
        'platformVersion': '7.1.3',  # 系统版本号
        'appPackage': 'com.xiaomi.shop',  # APP包名
        "noReset":True,
        "fllReset":False,
        'appActivity': 'com.xiaomi.shop2.activity.MainActivity'  # 启动页
    }
    def __init__(self):
        self.driver=webdriver.Remote(self.server, self.desired_capabilities)
        self.driver.implicitly_wait(10)


    def Order(self):
        self.driver.find_element_by_id("com.xiaomi.shop.plugin.homepage:id/searchIcon").click()
        self.driver.find_element_by_id("com.xiaomi.shop2.plugin.search:id/input").send_keys("小米平板5")
        self.driver.find_element_by_id("com.xiaomi.shop2.plugin.search:id/search_fragment_search_btn").click()
        self.driver.find_element_by_id("com.xiaomi.shop2.plugin.search:id/product_title").click()
        self.driver.find_element_by_id("com.xiaomi.shop2.plugin.goodsdetail:id/action_text_org").click() #抢购点击预约
        # self.driver.find_element_by_id("com.xiaomi.shop2.plugin.goodsdetail:id/action_quick_buy").click() #普通购买
        print("点击已预约")
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '白色')]").click()
        print("选择机器颜色配置")
        while True:
            buy="com.xiaomi.shop2.plugin.goodsdetail:id/buy"
            submit="com.xiaomi.shop2.plugin.shopcart:id/submit"
            self.driver.find_element_by_id("com.xiaomi.shop2.plugin.goodsdetail:id/action_text_org").click() #点击确认购买
            starttime = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
            print("%s确认配置并购买"%(starttime))
            current=self.driver.current_activity
            if current != "com.xiaomi.shop2.plugin.PluginRootActivity":
                try:
                    self.driver.find_element_by_id(buy).click()
                    print("添加购物车")
                    self.driver.find_element_by_id(submit).click() #点击去付款，生成订单
                    print("去付款")
                    self.driver.find_element_by_id("com.xiaomi.shop2.plugin.shopcart:id/text_pay_btn_pre").click()  # 点击确认支付
                    print("确认支付，生成订单")
                except:
                    self.driver.find_element_by_id(submit).click()  # 点击去付款，生成订单
                    print("不用添加购物车，直接付款")
                    self.driver.find_element_by_id("com.xiaomi.shop2.plugin.shopcart:id/text_pay_btn_pre").click()  # 确认付款
                    print("确认支付，生成订单")
            else:
                self.driver.find_element_by_id("com.xiaomi.shop2.plugin.goodsdetail:id/action_text_org").click() #点击确认购买
                loctime=time.strftime("%y-%m-%d %H:%M:%S",time.localtime())
                print("%s确认购买该机器"%(loctime))

# 立即购买="com.xiaomi.shop2.plugin.goodsdetail:id/action_quick_buy"
# 确认购买配置="com.xiaomi.shop2.plugin.goodsdetail:id/action_text_org"
# 不一定存在该步骤，购物车去结算="com.xiaomi.shop2.plugin.goodsdetail:id/buy"
# 去付款="com.xiaomi.shop2.plugin.shopcart:id/submit"
# 确认支付="com.xiaomi.shop2.plugin.shopcart:id/text_pay_btn_pre"
if __name__ == '__main__':
    go=GetOrder()
    go.Order()