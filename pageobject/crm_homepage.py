# coding=utf-8
import sys
sys.path.append(r"F:\selenium-py")
from framework.base_page import BasePage


class HomePage(BasePage):
    # CRM系统
    crm = "xpath=>.//*[@id='ea-system']/li[5]"

    def click_crm(self):
        self.click(self.crm)

    #----------------客户导入--------------
    # 客户导入
    khdr_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/p"
    # 新建客户
    xjkh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[1]/p"

    def click_khdr(self):
        self.click(self.khdr_btn)

    def click_xjkh(self):
        self.click(self.xjkh_btn)
