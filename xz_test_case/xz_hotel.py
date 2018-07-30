# coding=utf-8
import time
import unittest, sys
from selenium import webdriver
sys.path.append(r"F:\\selenium-py\\")
sys.path.append("\public")
from framework import longin
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from framework import myunit
from pageobject.xz_homepage import HomePage


class Start(myunit.MYtest):
    """酒店管理"""

    def test1(self):
        """客房信息"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_xzfw()

        homepage.click_jdgl1()

        homepage.sleep(0.1)

        homepage.click_kfxx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/guestRoomSearchPre.action']"))

        driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").get_attribute("value")
        a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")


    #@unittest.skip()
    def test2(self):
        """客房预订"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_xzfw()

        homepage.click_jdgl()

        homepage.sleep(0.1)

        homepage.click_tygsq()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/guestRoomBookSearchPre.action']"))

        driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")


if __name__ == '__main__':
    unittest.main()