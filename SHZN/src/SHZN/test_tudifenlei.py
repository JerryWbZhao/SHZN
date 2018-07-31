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
class tudifenlei(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://202.98.201.112:99/#/?nav=aa101531289117000001"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #土地分类用例
    def test_shzn_tudifenlei(self):
        u"""土地分类用例"""
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        #进入土地分类             
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div[2]/ul/li[2]").click()        
        time.sleep(3)
        #进入土地利用现状
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[1]").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layui-layer1']/span[1]/a[3]").click()
        time.sleep(3)
        #进入宗地区域管理
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layui-layer2']/span[1]/a[3]").click()
        time.sleep(3)
        #进入行政地区管理
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[3]").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layui-layer3']/span[1]/a[3]").click()
        time.sleep(3)
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(tudifenlei("test_shzn_tudifenlei"))
    results = unittest.TextTestRunner().run(suite)    