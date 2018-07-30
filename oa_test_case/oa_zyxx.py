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
	"""重要信息批露"""

	def test1_zyxxol(self):
		"""重要信息批露"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)

		homepage.click_zqgl()
        
		homepage.click_zyxx()

		homepage.sleep(0.1)

		homepage.click_zyxx2()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/informationPublishSearchPreAction.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_dbsjwh(self):
		"""担保数据维护"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)

		homepage.click_zqgl()
        
		homepage.click_zyxx()

		homepage.sleep(0.1)

		homepage.click_dbsjwh()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/guaranteeSearchPreAction.do']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a," 查询 ")
		homepage.get_page_title()
		print("***测试通过***")

	def test3_lhghgs(self):
		"""两会过会公司"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)

		homepage.click_zqgl()
        
		homepage.click_zyxx()

		homepage.sleep(0.1)

		homepage.click_lhghgs()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/twoSessionsCompanySearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("//*[@onclick='Search()']").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"查询")
		homepage.get_page_title()
		print("***测试通过***")



	def test4_zjdbsq(self):
		"""资金担保申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)

		homepage.click_zqgl()
        
		homepage.click_zyxx()

		homepage.sleep(0.1)

		homepage.click_zjdbsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/adFundguaranteeSearchPre.do']"))

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