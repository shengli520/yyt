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
	"""系统管理"""

	def test1_xtgl(self):
		"""系统日志查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_xtgl()

		homepage.sleep(0.1)

		homepage.click_xtrzxc()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/operationlogSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询  ")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_djsh(self):
		"""单据审核"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_xtgl()

		homepage.sleep(0.1)

		homepage.click_djsh()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/home.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")


	def test3_djsh(self):
		"""帮助文档"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_xtgl()

		homepage.sleep(0.1)

		homepage.click_bzwd()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/pubDocumentSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")

	def test4_djsh(self):
		"""MQ日志查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_xtgl()

		homepage.sleep(0.1)

		homepage.click_mqrzcx()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/mqLogForwardAction.do']"))

		driver.find_element_by_xpath("html/body/div[2]/div/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		a=driver.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td[3]/div/span[1]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"方向")
		homepage.get_page_title()
		print("***测试通过***")



	def test5_djsh1(self):
		"""系统执行时长报表"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_xtwh()

		homepage.click_xtgl()

		homepage.sleep(0.1)

		homepage.click_xtzxscbb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/systemExecuTimeActionPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search(this);']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search(this);']").get_attribute("value")

		#a=driver.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td[3]/div/span[1]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")


if __name__ == '__main__':
	unittest.main()