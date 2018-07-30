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
	"""项目分摊管理"""

	def test1_ywbmdr(self):
		"""业务部门导入"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_xmftgl()

		homepage.sleep(0.2)

		homepage.click_ywbmdr()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/organSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询 ")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#
	def test2_xmqddr(self):
		"""项目清单导入"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_xmftgl()

		homepage.sleep(0.2)

		homepage.click_xmqddr()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/inventoryProjectSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test3_xmftry(self):
		"""项目分摊人员"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_xmftgl()

		homepage.sleep(0.2)

		homepage.click_xmftry()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/projectStaff.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test4_ryxmzb(self):
		"""人员项目占比"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_xmftgl()

		homepage.sleep(0.2)

		homepage.click_ryxmzb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/staffProjectRatio.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询 ")
		homepage.get_page_title()
		print("***测试通过***")


if __name__ == '__main__':
	unittest.main()