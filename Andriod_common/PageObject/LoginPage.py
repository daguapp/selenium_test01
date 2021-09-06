from Andriod_common.BaseOperator.BaseElements import BaseElement
class Login:
 """登录页面的元素集合"""
 def __init__(self):
     self.el=BaseElement()

 def inputacount(self,acount): #输入账号
     self.el.locate_id("com.pengda.mobile.hhjz:id/et_mobile").send_keys(acount)

 def inputpassword(self,password): #输入密码
     self.el.locate_id("com.pengda.mobile.hhjz:id/et_pwd").send_keys(password)

 def clickbutton(self): #点击登录
     return self.el.locate_id("com.pengda.mobile.hhjz:id/btn_login").click()