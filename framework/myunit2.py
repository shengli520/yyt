# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time,re,sys
sys.path.append(r"F:\\selenium-py\\")
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger(logger="MYtest").getlog()

# 加启动配置

option = webdriver.ChromeOptions()

option.add_argument('disable-infobars')

class MYtest(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()