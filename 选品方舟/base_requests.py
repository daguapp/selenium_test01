import requests
from 选品方舟.get_token import login
class SendRequest(login):
    """封装requests请求"""

    def reflect(self,method,url,headers,**kwargs):
            #封装request方法，参数自定义
            result=requests.request(method=method,url=url,headers=headers,data=None)
            #获取响应状态码
            respond_code=result.status_code
            #获取响应文本
            respond_text=result.text
            #返回响应状态码和文本信息
            return respond_text and respond_code









