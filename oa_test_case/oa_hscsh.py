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
	"""核算初始化"""


	def test_hscsh(self):
		"""核算初始化"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_cwgl()

		homepage.click_hscsh()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://ehr.eascs.com/finBudgetManageByAccount.action?isReturn=NO']"))

		homepage.switch_frame("leftFrame")


		#driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法


		#展开菜单
		driver.find_element_by_xpath("//tr[@id='datagrid-row-r2-2-42603']/td[2]/div/span").click()

		# 断言
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()
		# 关闭窗口 

		homepage.back_frame()
		
		driver.find_element_by_xpath("/html/body/div/div[2]/ul/i").click()



if __name__ == "__main__":
    unittest.main()