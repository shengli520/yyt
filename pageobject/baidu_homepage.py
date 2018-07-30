# coding=utf-8
import sys
sys.path.append(r"F:\\selenium-py\\")
from framework.base_page import BasePage



class Baidu(BasePage):

    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)