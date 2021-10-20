import requests
class login:
    """获取登录token"""
    #定义一个实例
    def token(self,url,json,data,**kwargs):
        result=requests.post(url=url,json=None,data=None)
        if result.status_code == 200:
            try:
                # 获取登录成功账号cookie
                cookies=result.cookies
                return cookies
            except Exception as e:
                print("获取cookie失败，返回报错：%s"%(e))
        else:
            fail_code=result.status_code
            fail_text=result.text
            print("登录失败，请检查原因,返回状态码：%s，结果：%s"%(fail_code,fail_text))



