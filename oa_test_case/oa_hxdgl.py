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
	"""核销单管理"""

	def test1_hxdcx(self):
		"""核销单查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_hxdgl()

		homepage.sleep(0.2)

		homepage.click_hxdcx()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/cancellationPaperSearchPre.do']"))

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
	def test2_hxdsq(self):
		"""核销单申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_hxdgl()

		homepage.sleep(0.2)

		homepage.click_hxdsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/cancellationPaperRequestSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")
if __name__ == '__main__':
	unittest.main()