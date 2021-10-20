from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from tqdm import tqdm
from novels.inpuname import input_name
from novels.dir_name import dir
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
import requests
from selenium.webdriver.common.by import By

class GetNovels():
    #实例化浏览器对象
    def __init__(self,name):
        self.driver=webdriver.Chrome()
        self.url="https://www.xbiquge.la/"
        self.driver.get(self.url)
        self.novels_name=name
    def get_catalog(self):
            try:
                self.driver.find_element(By.ID,"wd").send_keys(self.novels_name)
                self.driver.find_element(By.ID,"sss").click()
                #跳转小说详情页面
                self.driver.find_element(By.LINK_TEXT,self.novels_name).click()
                #切换页面
                windows=self.driver.window_handles
                self.driver.switch_to.window(windows[-1])
                # 获取每一章的名称和url
                article=[]
                all_url=self.driver.find_elements(By.XPATH,'//div[@class="box_con"]/div/dl/dd/a')
                for i in range(0,len(all_url)-1):
                    article.append((all_url[i].text,all_url[i].get_attribute("href")))
                return article,self.driver
            except:
                print("找不到这本书")
    def get_content(self):
                #返回url和title
                eles,driver=self.get_catalog(),self.driver
                #循环遍历url获取网页内容
                file=dir(self.novels_name)
                for x in tqdm(eles):
                    for y in x:
                        try:
                            time.sleep(4)
                            self.driver.get(y[1])
                            els = self.driver.find_element(By.ID, "content")
                            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(els))
                        except :
                            self.driver.refresh()
                        finally:
                                print(">"*30+"正在下载"+y[0]+">"*30)
                                name="/"+f"{y[0]}"
                                els = self.driver.find_element(By.ID, "content")
                                with open(str(file)+str(f"{name}")+".txt","w",encoding="utf-8") as f:
                                        print(str(file)+str(f"{y[0]}")+".txt")
                                        f.write(els.text)

if __name__ == '__main__':
    do=GetNovels(input_name())
    do.get_content()
