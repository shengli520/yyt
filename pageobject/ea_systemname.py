# coding=utf-8
from framework.base_page import BasePage


class SyhomePage(BasePage):
    # OA系统
    oa_btn = "partial_link_text=>OA系统"

    # 行政系统
    xzbg = "partial_link_text=>行政系统"

    # e-HR系统
    ehr = "partial_link_text=>e-HR系统"

    # CRM系统
    crm = "partial_link_text=>CRM系统"

    def click_oa(self):
        self.click(self.oa_btn)
        self.sleep(0.5)

    def click_xzbg(self):
        self.click(self.xzbg)
        self.sleep(0.5)

    def click_ehr(self):
        self.click(self.ehr)
        self.sleep(0.5)

    def click_crm(self):
        self.click(self.crm)
        self.sleep(0.5)
