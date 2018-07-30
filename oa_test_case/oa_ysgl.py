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
	"""预算管理"""

	def test1_yssq(self):
		"""预算申请"""
		driver = self.driver
		driver.get(self.base_url)

		longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_cwgl()

		homepage.click_ysgl()

		homepage.sleep(0.3)

		homepage.click_yssq()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/finBudgetApplyManageSearchPreAction.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_ysbm(),"预算部门")
		homepage.get_page_title()
		print("***测试通过***")

	def test2_ystz(self):
		"""预算调整"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_cwgl()

		homepage.click_ysgl()

		homepage.sleep(0.4)

		homepage.click_ystz()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/finBudgetAdjustManageSearchPreAction.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_ysnd(),"预算年度")

		homepage.get_page_title()

		print("***测试通过***")

		# 
		# 
	def test3_edgl(self):
		"""额度管理"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_cwgl()

		homepage.click_ysgl()

		homepage.sleep(0.4)

		homepage.click_edgl()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/finBudgetAccountApplySearchPreAction.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_edlx(),"额度类型")

		homepage.get_page_title()

		print("***测试通过***")


	def test4_edblsq(self):
		"""额度比例申请"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_cwgl()

		homepage.click_ysgl()

		homepage.sleep(0.4)

		homepage.click_edblsq()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/finAccountingRatioSearchPre.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search();']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_billcode(),"单据编号")

		homepage.get_page_title()

		print("***测试通过***")


	def test5_edbb(self):
		"""额度报表"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_cwgl()

		homepage.click_ysgl()

		homepage.sleep(0.4)

		homepage.click_edbb()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/finBudgetAccountingReportUnitSearchPreAction.do']"))


		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_nd(),"年度")

		homepage.get_page_title()

		print("***测试通过***")


		# 关闭窗口 

		homepage.back_frame()
		
		driver.find_element_by_xpath("/html/body/div/div[2]/ul/i").click()


		#self.driver.quit()



if __name__ == "__main__":
    unittest.main()