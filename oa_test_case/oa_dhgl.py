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
	"""400电话管理 """

	def test1_fasp(self):
		"""400电话管理 """
		driver = self.driver
		driver.get(self.base_url)

		#longin.login(self)

		# 初始化业务合同查询主页对象
		homepage = HomePage(self.driver)

		homepage.click_oa()

		homepage.sleep(0.5)
        
		homepage.click_yygl()

		homepage.click_dhgl()

		homepage.switch_frame(driver.find_element_by_xpath("//iframe[@src='http://oa2.eascs.com/eaoa/phoneSearchPre.action']"))

		driver.find_element_by_xpath("//*[@onclick='btnSearch()']").click()
		#driver.refresh()
		a=driver.find_element_by_id("btnNew").get_attribute("value")

		homepage.get_windows_img()  # 调用基类截图方法

		# 断言
		self.assertEqual(a,"关闭申请")
		homepage.get_page_title()
		print("***测试通过***")

		# 关闭窗口 

		homepage.back_frame()
		
		driver.find_element_by_xpath("/html/body/div/div[2]/ul/i").click()
if __name__ == '__main__':
	unittest.main()