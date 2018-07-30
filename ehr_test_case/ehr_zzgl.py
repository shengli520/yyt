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
    """组织管理"""

    def test_01(self):
        """组织机构查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_zzjgcx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/departmentFrameworkSearch.action?isReturn=NO']"))
        homepage.switch_frame("leftFrame")

        driver.find_element_by_css_selector(".l-btn-text").click()
        # driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        a = driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test_02(self):
        """组织机构调整"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_zzjgtz()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/organadjustSearchPre.action?isReturn=NO']"))
        # homepage.switch_frame("leftFrame")

        # driver.find_element_by_css_selector(".l-btn-text").click()
        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_03(self):
        """组织机构审核人"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_zzjgshr()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/organauditorSearchPreAction.do']"))

        homepage.switch_frame("leftFrame")

        driver.find_element_by_css_selector(".l-btn-text").click()
        # driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        a = driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test_04(self):
        """单位管理"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_dwgl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/unitsManagePreAction.do']"))
        # homepage.switch_frame("leftFrame")

        # driver.find_element_by_css_selector(".l-btn-text").click()
        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search();']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_05(self):
        """单位审核人查询"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_dwshrcx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/unitsRoleEmployeeSearchPreAction.do']"))
        # homepage.switch_frame("leftFrame")

        # driver.find_element_by_css_selector(".l-btn-text").click()
        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_06(self):
        """绩效单位查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_jxdwcx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/performanceOrganMainPre.action?isReturn=NO']"))
        homepage.switch_frame("leftFrame")

        a = driver.find_element_by_css_selector(".tree-title").text
        # driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertIn("怡亚通", a)
        homepage.get_page_title()
        print("***测试通过***")

    def test_07(self):
        """绩效单位树预算"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_jxdwsys()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://ehr.eascs.com/performanceTreeBudgetDeptMainPre.action?isReturn=NO']"))
        homepage.switch_frame("leftFrame")

        a = driver.find_element_by_css_selector(".tree-title").text
        # driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "怡亚通")
        homepage.get_page_title()
        print("***测试通过***")

    def test_08(self):
        """绩效单位管理"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_jxdwgl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/performanceUnitManageSearchPre.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_09(self):
        """绩效单位申请"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_jxdwsq()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/performanceUnitApplySearchPreAction.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")

    def test_10(self):
        """绩效单位办理"""
        driver = self.driver
        driver.get(self.base_url)

        # longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_ehr()

        homepage.sleep(0.5)

        homepage.click_zzgl1()

        homepage.sleep(0.1)

        homepage.click_jxdwbl()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/performanceUnitHandleSearchPreAction.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search()']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath(
            "//*[@onclick='Search()']").get_attribute("value")
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").text
        # a=driver.find_element_by_css_selector(".l-btn-text").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")
        homepage.get_page_title()
        print("***测试通过***")


if __name__ == '__main__':
    unittest.main()
