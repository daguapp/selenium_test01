# -*- coding:utf-8 -*-
import json
from pathlib import Path
#
# Test.test_01()
# Test.test_02()

# lsita=["哈哈1","哈哈2","哈哈3"]
# test="哈哈"
# # assert test in lsita
# for i in lsita:
#     if test in i:
#         print(f"{i}断言通过")
#     else:
#         print(f"{i}断言失败")
# 反向范围取值 - 字符串
# def fib(max):
#     n=0
#     a, b = 0, 1
#     while n<max:
#         print(b)
#         a, b = b, a + b
#         n+=1


# from tqdm import tqdm
# def test():
#     for i in tqdm(range(10000000)):
#         temp = ['你好'] * 2000
#         yield temp
#
# a = test()
# for ele in a:
#     print(ele)
#     continue

# class Test01:
#     name="小明"
#     __instance=None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             print("分配实例对象内存，返回引用给__init__")
#             __instance=super().__new__(cls)
#             return cls.__instance
#
#     def __init__(self):
#         print("接收__new__返回实例对象的引用，开始执行构造方法")
#
#     def __test_get(self,a,b):
#         return a+b

# class Test:
#     __name="小明"
#
#     def __age(self):
#         print("%s是个学生"%(self.__name))
#
# t=Test()
# Test()._Test__age()
# print(t._Test__name)





# class Test01:
#     driver=None
#     def __new__(cls, *args, **kwargs):
#         if cls.driver is None:
#             cls.driver=super().__new__(cls)
#             print("没有实例时，返回实例对象id：%s"%(id(cls.driver)))
#         return cls.driver
#
#     def __init__(self):
#         print("开始执行构造方法")
#         print("构造方法id：%s"%(id(self)))
#
# t=Test()
# setattr(Test01,"driver",True)
# print(getattr(Test01,"driver"))
