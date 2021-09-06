from Andriod_common.PageObject.LoginPage import Login
import pytest
class CaseLogin:
    """登录页面测试流程"""
    def __init__(self):
        self.lg=Login()
    @pytest.mark.parametrize("acount,password",[('18582339746','19960122nm')])
    def test_login(self,acount,password):
        self.lg.inputacount(acount)
        self.lg.inputpassword(password)
        self.lg.clickbutton()
