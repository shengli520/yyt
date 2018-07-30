# coding=utf-8
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
	"""库存管理"""

	def test1_ckgl(self):
		"""仓库管理"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_kcgl()

		homepage.sleep(0.2)

		homepage.click_ckgl()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/warehousemanagesearchpre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#
	def test2_cksyl(self):
		"""仓库使用率"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_kcgl()

		homepage.sleep(0.2)

		homepage.click_cksyl()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/adStorageUsageSearchPreAction.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
	def test3_yscl(self):
		"""运输车辆"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_kcgl()

		homepage.sleep(0.2)

		homepage.click_yscl()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/vehicleSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#
	def test4_wlzyhz(self):
		"""物流资源汇总"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_kcgl()

		homepage.sleep(0.2)

		homepage.click_wlzyhz()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/logisticsPreSearch.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='btnSearch()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#
	def test5_clxxtjb(self):
		"""车辆信息统计表"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_kcgl()

		homepage.sleep(0.2)

		homepage.click_clxxtjb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/vehiclestatisticsPreSearch.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='btnSearch()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#

		#


if __name__ == "__main__":
    unittest.main()