# # coding=utf-8
# import time
# import unittest,sys
# from selenium import webdriver
# sys.path.append(r"F:\\selenium-py\\")
# from framework import longin
# from framework.browser_engine import BrowserEngine
# from framework.base_page import BasePage
# from pageobject.oa_homepage import HomePage
# from pageobject.ea_systemname import SyhomePage



# class IT_query(unittest.TestCase):

#     def setUp(self):
#         """
#         测试固件的setUp()的代码，主要是测试的前提准备工作
#         :return:
#         """
#         browse = BrowserEngine(self)
#         self.driver = browse.open_browser(self)

#     def tearDown(self):
#         """
#         测试结束后的操作，这里基本上都是关闭浏览器
#         :return:
#         """
#         self.driver.refresh()

#     def test_IT_query(self):
#         """
#         这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
#         :return:
#         """
#         # 调用登陆
#         longin.login(self)

#         # 调用页面
#         # 初始化基类对象
#         #base_page = BasePage(self.driver)

#         # 初始化业务合同查询主页对象
#         homepage = HomePage(self.driver)

#         homepage.click_oa()
#         homepage.sleep(0.5)


#         homepage.click_eatxl()

#         homepage.click_ygtxl()


#         homepage.switch_frame(self.driver.find_element_by_xpath("//iframe[@src='employeeContactPre.do']"))

#         homepage.click_who()

#         self.driver.find_element_by_xpath("//*[@onclick='Search()']").click()
#         #driver.refresh()

#         homepage.get_windows_img()  # 调用基类截图方法

#         self.assertEqual(homepage.get_text(),"员工工号")
#         homepage.get_page_title()
#         print("***测试通过***")
       
#             #assert '员工工号' in homepage.get_txt()  # 调用页面对象继承基类中的获取页面标题方法
#             #itle = self.driver.find_element_by_id("employeecode").text

#             #self.assertEqual(title, "中文名")
#         # try:
#         #     self.assertEqual(homepage.get_text(),"员工工号")
#         #     print ('**测试通过**')
#         # except Exception as e:
#         #     print ('**测试失败**.', format(e))

# if __name__ == '__main__':
#     unittest.main()
#     
# for i in range(10):
#     if i % 2 !=0:
#         print(i)

# user="shengli.zheng"
# passwd="qazx369020547ZSL@"

# for i in range(3):
#     username= input("username:")
#     password= input("password:")

#     if username==user and passwd ==password:
#         print("欢迎回来 %s " % username)
#         break
#     else:
#         print("账号或者密码错误")
# else:
#     print("登陆测试太多")

num=1

while num<=100:
    if num %2 ==0:
        print(num)

    num = num + 1

