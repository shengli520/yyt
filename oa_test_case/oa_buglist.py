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
	"""BUG-LIST"""

	def test1_bug(self):
		"""bug"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_itfw()

		homepage.click_buglist()

		homepage.sleep(0.1)

		homepage.click_bug()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://gc.eascs.com/bug/bugmanage']"))

		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div/span[2]/span/button").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/div[2]/table/thead/tr/th[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"BUG编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_bug(self):
		"""版本"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_itfw()

		homepage.click_buglist()

		homepage.sleep(0.1)

		homepage.click_bb()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://gc.eascs.com/bug/bugversion']"))

		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div/span[2]/span/button").click()
		#driver.refresh()
		#a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")
		a=driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/div[2]/table/thead/tr/th[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"版本号")
		homepage.get_page_title()
		print("***测试通过***")


if __name__ == '__main__':
	unittest.main()