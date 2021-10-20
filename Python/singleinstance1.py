from selenium import webdriver
from singleinstance import  singe
class singe1:
    def __init__(self):
        B=singe()
        print(id(B))


if __name__ == '__main__':
    C=singe1()



