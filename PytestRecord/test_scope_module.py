import pytest
"""scope=module时表示当前.py文件中被多次调用，只会执行一次"""
@pytest.fixture(scope="module")
def test_one():
    print("这是首个测试用例module")

class Test01:

    def test_01(self,test_one,test_primary):
        print(test_primary)
        print(test_one)
        print("这是第一个测试用例")


class Test02:
    def test_02(self,test_one):
        print(test_one)
        print("这是第二个测试用例")
if __name__ == '__main__':
    pytest.main(["-q","test_scope_module.py"])