from selenium import webdriver

class singe:
    def __new__(cls, *args, **kwargs):
        if  hasattr(cls,"instance") == False:
            instance=super().__new__(cls)
            return instance

    def __init__(self):
        self.driver=webdriver.Chrome()
        print(id(self.driver))







