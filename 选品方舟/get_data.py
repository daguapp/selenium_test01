import openpyxl

class GetData:
    """打开excel获取并修改数据"""

    def __init__(self,path,sheet):
        #传入exel路径，生成工作簿打开文件
        self.form=openpyxl.load_workbook(path)
        #选取表单
        self.sheet=self.form[sheet]

    def cell_data(self,row,col):
        #输入行和列
        ce=self.sheet.cell(row,col)
        #返回单元格数据
        return ce

    def row_data(self):
        #按行读取数据
        col=list(self.sheet.rows)
        return col

    def col_data(self):
        #按列读取数据
        row=list(self.sheet.columns)
        return row
    def cell_value(self,index):
        value=self.sheet[index].value
        return value
if __name__ == '__main__':
    g=GetData(r"C:\Users\admin\Desktop\interface.xlsx","Sheet1")
    print(g.cell_value("A1"))