#coding=utf-8
import time
import unittest,sys
from selenium import webdriver
sys.path.append(r"F:\\selenium-py\\")
sys.path.append("\public")
from framework import longin
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from framework import myunit
from pageobject.oa_homepage import HomePage


class Start(myunit.MYtest):
	"""审计管理"""

	def test1_sjjb(self):
		"""审计简报"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_sjgl()

		homepage.click_sjjb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/auditingReportFrameSearchPre.action?dbClickUrl=auditingReportSearch.action']"))

		homepage.switch_frame("manageFrame")

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='btnSearch()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[3]/table/tbody/tr[1]/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"公司名称")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_sjjh(self):
		"""审计计划"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_sjgl()

		homepage.click_sjjh()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/auditingPlanFrameSearchPre.action?dbClickUrl=auditingPlanSearch.action']"))

		homepage.switch_frame("manageFrame")

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='btnSearch()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[3]/table/tbody/tr[1]/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"公司名称")
		homepage.get_page_title()
		print("***测试通过***")

if __name__ == '__main__':
	unittest.main()