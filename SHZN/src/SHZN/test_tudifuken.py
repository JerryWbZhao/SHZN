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
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, os
import HTMLTestRunner
class tudifuken(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://202.98.201.112:99/#/?nav=aa101531289117000001"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #土地复垦用例
    def test_shzn_tudifuken(self):
        u"""土地复垦用例"""
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        #进入土地复垦            
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div[2]/ul/li[5]").click()        
        time.sleep(3)
        #进入土地复垦方案
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[1]").click()        
        time.sleep(3)
        #进入土地评价要素监管
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]/div").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]/ul/li[1]").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layui-layer1']/span[1]/a[3]").click()
        time.sleep(3)
        #进入土地复垦评价管理
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]/ul/li[2]").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layui-layer2']/span[1]/a[3]").click()
        time.sleep(3)
        #进入土地复垦措施
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[3]").click()        
        time.sleep(3)
        #进入土地绿化工程
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/ul/li[4]").click()        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='layui-layer3']/span[1]/a[3]").click()
        time.sleep(3)
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(tudifuken("test_shzn_tudifuken"))
    results = unittest.TextTestRunner().run(suite)    