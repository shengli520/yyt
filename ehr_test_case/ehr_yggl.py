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
    """员工管理"""

    def test_01(self):
        """员工档案"""
        driver = self.driver
        driver.get(self.base_url)

        longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_ygda()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/employeeManageSearchPre.do']"))

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
        """编外员工"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_bwyg()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/employeeOutManageSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
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
        """员工合同"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_yght()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeeContractManageSearchPre.action?isReturn=NO']"))

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

    def test_04(self):
        """人事异动"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_rsyd()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeeTurnoverSearchPreAction.action?isReturn=NO']"))

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

    def test_05(self):
        """实习生解约"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_sxsjy()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/traineeDismissalSearchPre.do']"))

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

    def test_06(self):
        """离职申请"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_lzsq()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeeDimissionManageSearchPre.action?isReturn=NO']"))

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

    def test_07(self):
        """离职交接"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_lzjj()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/employeeDimissionProcessManageSearchPre.action?isReturn=NO']"))

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

    def test_08(self):
        """追缴流程"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_zjlc()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/dimissionRecoveredSearchPre.action?isReturn=NO']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test_09(self):
        """户口调动"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_yggl()

        homepage.sleep(0.1)

        homepage.click_hkdd()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/residenceManageSearchPre.action?isReturn=NO']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")


if __name__ == '__main__':
    unittest.main()
