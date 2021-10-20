import requests
import pytest
import logging
from 选品方舟.get_data import GetData
import re
import 选品方舟.base_requests
class TestCase:
    """执行测试用例"""
    @pytest.fixture(scope="function",)
    @pytest.mark.parametrize("path,sheet",[r"C:\Users\admin\Desktop\interface.xlsx","Sheet1"])
    def test_01(self,path,sheet):
        #获取导入的数据
        ob=GetData(path,sheet)
        data=ob.row_data()
        list_data=[]
        for x in data:
            listb=[]
            for y in x:
                #正则匹配excel表内容的位置坐标
                index=re.findall("<Cell 'Sheet1'.(.*?)>",str(y))
                new_index=str(index).strip("[]")
                new_index=eval(new_index)
                value=ob.cell_value(new_index)
                if value != None:
                    listb.append(value)
            #拆分成每一行坐标为一组
            list_data.append(tuple(listb))
        return list_data
    def test_request(self):
        listdata=self.test_01
        print(listdata)
        for i in (listdata[1:]):
            print(i)







    def unpack_data(self):
        pass



if __name__ == '__main__':
    pytest.main()
