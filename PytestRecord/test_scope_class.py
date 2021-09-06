import pytest
"""fixture的作用范围"""
"""fixture一共有四种作用范围"""
"""scope=clss表示同一个clss被被多个用例调用时，只会执行一次"""
@pytest.fixture(scope="class")
def test_one():
    print("这是首个测试用例")

class TestScopeClass:

    def test_01(self,test_one,test_primary):
        print(test_primary)
        print(test_one)
        print("这是二号测试用例")

    def test_02(self,test_one):
        print(test_one)
        print("这是三号测试用例")
if __name__ == '__main__':
    pytest.main(["-q","test_scope_class.py"])