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
	"""诉讼案件归档管理"""

	def test1_ajjcxxb(self):
		"""案件基础信息表"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_ssgl()

		homepage.sleep(0.2)

		homepage.click_ajjcxxb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/basicDataSearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text
		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"档案编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_ajcxxxb(self):
		"""案件程序信息表"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_ssgl()

		homepage.sleep(0.2)

		homepage.click_ajcxxxb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/procedureDataSearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text
		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"案件程序编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test3_ajjdhbb(self):
		"""案件进度汇报表"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_ssgl()

		homepage.sleep(0.2)

		homepage.click_ajjdhbb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/rateReportSearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text
		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"案件程序编号")
		homepage.get_page_title()
		print("***测试通过***")


	def test4_ajjcxxb(self):
		"""报表统计"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_ssgl()

		homepage.sleep(0.2)

		homepage.click_bbtj()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/reportExportExcelPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text
		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"案件所属单位")
		homepage.get_page_title()
		print("***测试通过***")



if __name__ == '__main__':
	unittest.main()