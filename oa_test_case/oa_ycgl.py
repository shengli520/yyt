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
	"""异常管理"""

	def test1_yzyc(self):
		"""运作异常"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_ycgl()

		homepage.sleep(0.1)

		homepage.click_yzyc()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/discrepancySearchPre.do']"))

		homepage.sleep(0.1)

		driver.find_element_by_id("search").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_cybh(),"差异编号")
		
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#
	def test2_ycpcfy(self):
		"""异常赔偿费用"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_ycgl()

		homepage.sleep(0.1)

		homepage.click_ycpcfy()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/discrepancyfeeSearchPre.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_cybh(),"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		#
	def test3_yskkcyc(self):
		"""应收款库存异常"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_ycgl()

		homepage.sleep(0.1)

		homepage.click_yskkcyc()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/fundexceptionManageSearchPre.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_cybh(),"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
	def test4_hqzycx(self):
		"""货权转移查询"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_ycgl()

		homepage.sleep(0.1)

		homepage.click_hqzycx()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/goodstransferSearchPre.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_cydjbh(),"单据编号")
		homepage.get_page_title()
		print("***测试通过***")

		# 关闭窗口 

		homepage.back_frame()
		
		driver.find_element_by_xpath("/html/body/div/div[2]/ul/i").click()


		#self.driver.quit()


if __name__ == "__main__":
    unittest.main()