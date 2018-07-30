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
    """立政管理"""
    #@unittest.skip(111)
    def test1(self):
        """流程变更查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_lzgl()

        homepage.click_lcbgcx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/wfchargeChangeSearchPreAction.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")


    #@unittest.skip(11)
    def test2(self):
        """流程变更管理"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_lzgl()

        homepage.click_lcbggl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/wfchangeSearchMychangePreAction.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")


    def test3(self):
        """流程新建申请"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_lzgl()

        homepage.click_lcxjsq()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/demandmodifypre.do?isReturn=NO&from=LZ']"))

        driver.find_element_by_xpath("//*[@value='返回']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")


if __name__ == '__main__':
    unittest.main()