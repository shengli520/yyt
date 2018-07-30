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
    """培训管理"""

    def test_01(self):
        """讲师管理"""
        driver = self.driver
        driver.get(self.base_url)

        longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_jsgl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/trainlecturerSeachPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_02(self):
        """课程管理"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_kcgl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/traincourseSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test_03(self):
        """培训需求"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_pxxq()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/trainrequestSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_04(self):
        """培训计划"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_pxjh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/trainplanSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_05(self):
        """培训实施"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_pxss()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/trainpracticeSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_06(self):
        """培训历史查询"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_pxlscx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/trainhistorySearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_07(self):
        """试卷管理"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_sjgl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/traintestSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_08(self):
        """360反馈"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_pxgl()

        homepage.sleep(0.1)

        homepage.click_360fk()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/assessmentSearchPre.action']"))

        # driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_css_selector(
            ".datagrid-cell.datagrid-cell-c1-theme").text
        # a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "问卷主题")
        homepage.get_page_title()
        print("***测试通过***")


if __name__ == '__main__':
    unittest.main()
