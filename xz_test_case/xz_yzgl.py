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
from pageobject.xz_homepage import HomePage


class Start(myunit.MYtest):
	"""印章管理"""

	def test1_yzkzsq(self):
		"""印章刻制申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_xz()

		homepage.sleep(0.5)
        
		homepage.click_yzgl()

		homepage.click_yzkzsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/assetsStampManufactureSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_yzdjcx(self):
		"""印章登记查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_xz()

		homepage.sleep(0.5)

		homepage.click_yzgl()

		homepage.click_yzdjcx()

		homepage.switch_frame(driver.find_element_by_xpath(
			"//iframe[@src='http://oa2.eascs.com/eaoa/assetsStampSaveSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		# driver.refresh()
		a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a, "查询")
		homepage.get_page_title()
		print("***测试通过***")


	def test3_yzsysq(self):
		"""印章使用申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_xz()

		homepage.sleep(0.5)

		homepage.click_yzgl()

		homepage.click_yzsysq()

		homepage.switch_frame(driver.find_element_by_xpath(
			"//iframe[@src='http://oa2.eascs.com/eaoa/assetsStampUseSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		# driver.refresh()
		a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a, "查询")
		homepage.get_page_title()
		print("***测试通过***")

	def test4_jzbfsq(self):
		"""借转.报废申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_xz()

		homepage.sleep(0.5)

		homepage.click_yzgl()

		homepage.click_jzbfsq()

		homepage.switch_frame(driver.find_element_by_xpath(
			"//iframe[@src='http://oa2.eascs.com/eaoa/assetsStampBorrowSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		# driver.refresh()
		a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a, " 查询")
		homepage.get_page_title()
		print("***测试通过***")

	def test5_jzdjcx(self):
		"""借.转单据查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_xz()

		homepage.sleep(0.5)

		homepage.click_yzgl()

		homepage.click_jzdjcx()

		homepage.switch_frame(driver.find_element_by_xpath(
			"//iframe[@src='http://oa2.eascs.com/eaoa/assetsStampTransactionSearchPre.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		# driver.refresh()
		a = driver.find_element_by_xpath("//*[@onclick='Search();']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a, "查询")
		homepage.get_page_title()
		print("***测试通过***")


if __name__ == '__main__':
	unittest.main()