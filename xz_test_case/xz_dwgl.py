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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Start(myunit.MYtest):
    """单位管理"""

    def test1(self):
        """单位信息查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_dwgl()

        #homepage.click_kdgl()
        #ele = driver.find_element_by_xpath(".//*[@id='ea-scroll']/div/div[4]/div/div[7]/p")

        #ele.click()
        # menu_xpath = ".//*[@id='ea-scroll']/div/div[4]/div/div[7]/p"  # 更多产品XPATH
        # more_menu = WebDriverWait(driver=driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, menu_xpath)))
        # ActionChains(driver=driver).move_to_element(more_menu).perform()
        # time.sleep(3)  # 仅为能达到悬停效果睡眠，可删除

        #ActionChains(driver).move_to_element(ele).perform()

        time.sleep(0.1)

        homepage.click_dwxxcx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/unitsAdManagePreAction.do']"))

        driver.find_element_by_xpath("//*[@onclick='Search();']").click()
        # driver.refresh()
        a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

        print("获取查询按钮的文本: %s" % a)
        #a = driver.find_element_by_xpath("//*[@onclick='btnSearch()']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, " 查询 ")

        homepage.get_page_title()
        print("***测试通过***")


    def test2(self):
        """单位业务申请"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_dwgl()

        homepage.sleep(0.1)

        homepage.click_dwywsq()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/companyEstablishApplySearchPre.action']"))

        driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        a = driver.find_element_by_xpath("//*[@onclick='btnSearch();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")

    def test3(self):
        """业务进度查询"""
        driver = self.driver
        driver.get(self.base_url)

        #longin.login(self)

        # 初始化业务合同查询主页对象
        homepage = HomePage(self.driver)

        homepage.click_xz()

        homepage.sleep(0.5)

        homepage.click_dwgl()

        homepage.sleep(0.1)

        homepage.click_ywjdcx()

        homepage.switch_frame(driver.find_element_by_xpath(
            "//iframe[@src='http://oa2.eascs.com/eaoa/companyEstablishDoSearch.action']"))

        driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
        # driver.refresh()
        #a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
        a = driver.find_element_by_xpath("//*[@onclick='btnSearch();']").text

        homepage.get_windows_img()  # 调用基类截图方法

        # 断言
        self.assertEqual(a, "查询")
        homepage.get_page_title()
        print("***测试通过***")


if __name__ == '__main__':
    unittest.main()