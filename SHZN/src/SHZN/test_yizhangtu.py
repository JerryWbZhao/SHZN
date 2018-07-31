#coding=utf-8
'''
Created on 2018年7月31日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class yizhangtu(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://202.98.201.112:99/#/?nav=aa101531289117000001"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #一张图用例
    def test_shzn_yizhangtu(self):
        u"""一张图用例"""
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)      
        driver.switch_to.frame('aa101531289117000001')       
        time.sleep(3)       
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='map']/div[1]/div[6]/div/div[1]/div/div/div/div[2]/div/a").click()        
        time.sleep(3)
        try:
        #是一个无法找到的元素id
            driver.find_element_by_xpath("//*[@id='layout']/section/aside[6]/div/div[3]/button[4]/span")
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\yizhangtu.png")
        #如果没有找到上面的元素就截取当前页面。
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layout']/section/aside[6]/div/div[3]/button[4]/span").click()
        time.sleep(3)
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(yizhangtu("test_shzn_yizhangtu"))
    results = unittest.TextTestRunner().run(suite)    