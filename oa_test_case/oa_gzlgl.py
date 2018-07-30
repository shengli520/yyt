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
from selenium.webdriver.support.select import Select


class Start(myunit.MYtest):
	"""工作流管理"""

	def test1_shryl(self):
		"""流程审核人预览"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_gzlgl()

		homepage.sleep(0.1)

		homepage.click_lcshryl()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/wfAuditorViewPre.do']"))

		homepage.switch_frame("manageFrame")

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_lcshrcx(self):
		"""流程审核人查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_gzlgl()

		homepage.sleep(0.1)

		homepage.click_lcshrcx()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/wfAuditorSearchForCsPre.do?isReturn=NO']"))

		Select(driver.find_element_by_id("processtype")).select_by_value("LBS")

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")


	def test3_lcbgsp(self):
		"""流程变更审批"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_gzlgl()

		homepage.sleep(0.1)

		homepage.click_lcbgsp()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/wfchargeChangeSearchPreAction.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test4_szlclb(self):
		"""设置流程类别管理员"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_gzlgl()

		homepage.sleep(0.1)

		homepage.click_szlclb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/wfManagerFramePre.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询 ")
		homepage.get_page_title()
		print("***测试通过***")



	def test5_czzy(self):
		"""操作指引"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_gzlgl()

		homepage.sleep(0.1)

		homepage.click_czzy()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/workflowGuide.do']"))

		# driver.find_element_by_xpath("//*[@onclick='Search(this);']").click()
		# #driver.refresh()
		# a=driver.find_element_by_xpath("//*[@onclick='Search(this);']").get_attribute("value")

		a=driver.find_element_by_css_selector("#results_table1>tbody>tr>td>a>font").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"流程管理员操作指引")
		homepage.get_page_title()
		print("***测试通过***")


if __name__ == '__main__':
	unittest.main()