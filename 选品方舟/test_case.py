import requests
import pytest
from get_data import *
import re
import base_requests
class TestCase:
    """执行测试用例"""
    @pytest.mark.parametrize("path,sheet",[r"C:\Users\admin\Desktop\interface.xlsx","Sheet1"])
    def setup_class(self,path,sheet):
        #获取导入的数据
        ob=GetData(path,sheet)
        data=ob.row_data()
        global list_data
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

    def test_request(self):
        for i in (list_data[1:]):
            print(i)





        print(list_data)

    def unpack_data(self):
        pass



if __name__ == '__main__':
    pytest.main()
