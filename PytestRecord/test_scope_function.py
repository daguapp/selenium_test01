import pytest
#如果导包失败，文件夹内缺少init文件
#调用方式一：@pytest.fixture修饰的函数作为参数传入另一个函数
#使用场景，只有部分用例需要登录登录就能执行的用例
#如果有多个参数返回时，可使用元祖的形式，再函数内拆分
@pytest.fixture #fixture没有返回值时默认为None，调用返回值直接将其装饰的函数作参数
def test_fix():
    """scope=function是默认作用范围，不填写时即默认function，每次调用之前执行一次"""
    print("这是一个变量")


def test_01(test_fix,test_primary):#直接使用函数名作为调用fixture的返回值
    print(test_primary)
    print(test_fix)     #方便用于部分用例需要登录的场景
    print("这是测试用例一")

if __name__ == '__main__':
    pytest.main(['-q', 'test_scope_function.py'])
