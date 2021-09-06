import pytest
"""使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例"""
"""需要使用test_01的返回参数时，需要使用参数传入，如果不需要返回参数，则两种方式皆可以"""
@pytest.fixture
def test_01():
    return 10

# @pytest.mark.usefixtures("test_01")

def test_02(test_01):
    print(test_01)
    print("11")
if __name__ == '__main__':
    pytest.main()