import os

def dir(name):
    file="D:/小说/" + name
    if os.path.exists(file):
        print(f"文件夹{name}已存在")
        return file
    else:
        os.mkdir(file)
        print(f"创建文件夹{name}成功")
        return file