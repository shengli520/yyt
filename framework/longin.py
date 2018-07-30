# -*- coding: utf-8 -*-
def login(self):
    driver = self.driver
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("shengli.zheng")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("qazx369020547ZSL")
    driver.find_element_by_name("submit").click()

