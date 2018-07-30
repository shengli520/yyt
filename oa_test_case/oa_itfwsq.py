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
	"""IT服务申请"""

	def test1_rjdjgl(self):
		"""软件登记管理"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_itfw()

		homepage.click_itfwsq()

		homepage.sleep(0.1)

		homepage.click_rjdjgl()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/softwaremanagesearchpre.do']"))

		homepage.sleep(0.1)

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_xnjsq(self):
		"""虚拟机申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_itfw()

		homepage.click_itfwsq()

		homepage.sleep(0.1)

		homepage.click_xnjsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/vmapplySearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"\xa0查询\xa0")
		homepage.get_page_title()
		print("***测试通过***")

	def test3_xttjsq(self):
		"""系统停机申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_itfw()

		homepage.click_itfwsq()

		homepage.sleep(0.1)

		homepage.click_xttjsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/stopServiceSearchPre.action?isReturn=NO']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test4_xttjrz(self):
		"""系统停机日志"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_itfw()

		homepage.click_itfwsq()

		homepage.sleep(0.1)

		homepage.click_xttjrz()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/stopServiceLogSearch.action?isReturn=NO']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr[1]/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"单据编号")
		homepage.get_page_title()
		print("***测试通过***")


if __name__ == '__main__':
	unittest.main()