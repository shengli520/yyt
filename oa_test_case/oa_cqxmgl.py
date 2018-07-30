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
	"""超期项目管理"""

	def test1_cqxmsq(self):
		"""超期项目申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_cqxmgl()

		homepage.sleep(0.1)

		homepage.click_cqxmsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/delaySearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_lshsq(self):
		"""律师函申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_cqxmgl()

		homepage.sleep(0.1)

		homepage.click_lshsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/lawyerLetterSearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test3_sscxsq(self):
		"""诉讼程序申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_cqxmgl()

		homepage.sleep(0.1)

		homepage.click_sscxsq()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/lawsuitApplySearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch();']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

	def test4_lshtj(self):
		"""律师函统计"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_fwgl()

		homepage.click_cqxmgl()

		homepage.sleep(0.1)

		homepage.click_lshtj()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/lawyerLetterSearchByCount.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		a=driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]").text

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"所属集群")
		homepage.get_page_title()
		print("***测试通过***")



if __name__ == '__main__':
	unittest.main()