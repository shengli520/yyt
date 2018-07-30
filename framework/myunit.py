# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time,re,sys
sys.path.append(r"F:\\selenium-py\\")
from framework.logger import Logger

logger = Logger(logger="MYtest").getlog()

# 加启动配置

option = webdriver.ChromeOptions()

option.add_argument('disable-infobars')

#return webdriver.Chrome(chrome_options = option,desired_capabilities = None)

dr = webdriver.Chrome(chrome_options=option)
logger.info("You had select %s browser." % dr)
#dr =webdriver.Firefox()
class MYtest(unittest.TestCase):
    def setUp(self, driver =dr):
        self.driver = driver
        self.driver.maximize_window()
        logger.info("browser maximize the current window." )
        self.driver.implicitly_wait(10)
        self.base_url = "http://oa.eascs.com/eaoa/"
        logger.info("Open browser url is: %s" % self.base_url)
        self.verificationErrors = []


    def tearDown(self):
        try:
            self.driver.refresh()
            time.sleep(0.4)
        except ConnectionRefusedError as e:
            print(e)
        finally:
            self.assertEqual([], self.verificationErrors)
