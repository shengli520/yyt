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
	"""员工通讯录"""

	def test_ygtxl(self):
		"""员工通讯录"""
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_eatxl()

		homepage.click_ygtxl()


		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/employeeContactPre.do']"))

		homepage.click_who()

		driver.find_element_by_xpath("//*[@onclick='Search()']").click()
		#driver.refresh()

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言

		self.assertEqual(homepage.get_text(),"员工工号")
		homepage.get_page_title()
		print("***测试通过***")

		#self.driver.quit()



if __name__ == "__main__":
    unittest.main()