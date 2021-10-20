from Andriod_common.PageObject.LoginPage import Login
import pytest
import logging
class TestLogin:
    """登录页面测试流程"""
    @pytest.mark.parametrize("acount,password",[('18582339746','19960122nm'),("18699018831","b123456")])
    def test_login(self,acount,password):
        self.lg=Login()
        self.lg.inputacount(acount)
        logging.log(logging.INFO,f"输入账号：{acount}")
        self.lg.inputpassword(password)
        logging.log(logging.INFO, f"输入密码：{password}")
        self.lg.clickbutton()
        logging.log(logging.INFO,"点击登录")
if __name__ == '__main__':
    pytest.main()
