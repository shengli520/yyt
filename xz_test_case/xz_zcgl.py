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
    """资产管理"""
    #@unittest.skip(111)
    def test1(self):
        """固定资产管理"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_zclysq()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsSearchpre.do']"))

        #driver.refresh()

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询  ")
        homepage.get_page_title()
        print("***测试通过***")


    #@unittest.skip(11)
    def test2(self):
        """资产领用申请"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_zccgcx()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsPurSearchpre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    #@unittest.skip(11)
    def test3(self):
        """转移单据查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_zydjcx()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsTransferSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test4(self):
        """报废单据查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_bfdjcx()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsScrapSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test5(self):
        """资产库查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_zckcx()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsStockSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test6(self):
        """借用单据查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_jydjcx()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsBorrowSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test7(self):
        """维修单据查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_wxdjcx()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsRepairSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test8(self):
        """盘点资产导入"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_pdzcdr()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/assetsStockTmpSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test9(self):
        """资产撤单申请"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_zcgl()

        homepage.click_gdzcgl()

        homepage.sleep(0.2)

        homepage.click_zccdsq()

        driver.refresh()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/fiBillCancelAstSearchPre.action']"))

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