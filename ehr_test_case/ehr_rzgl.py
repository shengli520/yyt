# coding=utf-8
import time
import unittest
import sys
from selenium import webdriver
sys.path.append(r"F:\\selenium-py\\")
from framework import longin
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from framework import myunit
from pageobject.ehr_homepage import HomePage


class Start(myunit.MYtest):
    """入职管理"""

    def test_01(self):
        """个人资料"""
        driver = self.driver
        driver.get(self.base_url)

        longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_rzgl()

        homepage.sleep(0.1)

        homepage.click_grzl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeenewPersonalDataSearchPre.action?isReturn=NO']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_02(self):
        """基础信息"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_rzgl()

        homepage.sleep(0.1)

        homepage.click_jcxx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeenewBasicDataSearchPre.action?isReturn=NO']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_03(self):
        """办公资料"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_rzgl()

        homepage.sleep(0.1)

        homepage.click_bgzl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeenewOfficeDataSearchPre.action?isReturn=NO']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")
if __name__ == '__main__':
    unittest.main()
