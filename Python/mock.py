import requests
import requests
import unittest
from unittest import mock
class client:

    def send_request(self,url):
        r = requests.get(url)
        return r.status_code


    def visit_ustack(self,url='http://www.ustack.com'):
        return self.send_request(url)


# class TestClient(unittest.TestCase):
#
#     def setUp(self):
#         self.cl=client()
#
#     def test_success_request(self):
#         self.cl.visit_ustack= mock.Mock(return_value='200')
#         self.assertEqual(self.cl.visit_ustack(), '200')
#
#     def test_fail_request(self):
#         self.cl.visit_ustack= mock.Mock(return_value='404')
#         self.assertEqual(self.cl.visit_ustack(), '404')
# if __name__ == '__main__':
#     unittest.main()
class TestFb():
    def __init__(self):
        self.a=0
        self.b=1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        num = self.a
        return num
iterator=TestFb()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
