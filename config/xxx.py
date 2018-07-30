#coding = utf-8
import requests

import json

url = "http://cas2.eascs.com/cas/login?locale=zh_CN&service=http://172.29.13.65:7001/eaoa/"

# date = {
#     "username": "shengli.zheng",
#     "password": "qazx369020547ZSL",
#     "lt": "LT-39089949-F9FIFeBeBlHcmWZjLINiUBclXXpIuz-cas.eascs.com",
#     "execution": "e2s1",
#     "_eventId": "submit",
#     "chartype": "zh_CN",
#     "submit": "登录"
# }

header = {
    "Host": "cas2.eascs.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://172.29.13.65:7001/eaoa/",
    "Accept-Encoding": "gzip, deflate",
    #"Cookie": "JSESSIONID=DDF32B2C9D9C74F963AE2C7008619817-n2; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN",
    "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8"
}

#cookies = {'JSESSIONID': 'F8E830D11DB0C4BBC367FA3F58D023CD-n1'}

res = requests.get(url=url, headers=header)

print(res.status_code)

print(res.headers)

print(res.text)

# print(res.text)

# res = json.dumps(res, indent=4)
# print(res)

# print(res.content)

# print(res)
#
# from selenium import webdriver

# import time

# driver=webdriver.Chrome()
# driver.maximize_window()

# driver.get("http://www.baidu.com")

# driver.implicitly_wait(2)

# #time.sleep(2)

# driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")

# #time.sleep(2)

# driver.implicitly_wait(2)

# driver.find_element_by_xpath(".//input[@id='su']").click()

# driver.implicitly_wait(2)

# print(driver.name)

# print(driver.title)

# print(driver.current_url)

# driver.quit()

# from selenium import webdriver
# import time
# import json
# dr = webdriver.Chrome()
# dr.maximize_window()

# dr.get("https://crm.xiaoshouyi.com/")
# dr.find_element_by_name('loginName').send_keys('17551086002')
# dr.find_element_by_name('password').send_keys('qq1084900')
# time.sleep(1)
# dr.find_element_by_xpath('.//*[@id="div_main"]/div[1]/div[1]/div[2]/a').click()

# t=input("这是是什么鬼")
# print("hello",t)

# import cx_Oracle

# conn1 = cx_Oracle.connect('eadb/eadbqa@172.29.12.46:1521/46')

# #conn1 = cx_Oracle.connect()

# c = conn1.cursor()

# x = c.execute('select * from pthon')

# print(x.fetchone())
