from selenium.webdriver.common.by import By

import sys,os
sys.path.append(".")
# print("x"*30)
# print(os.getcwd())
from api.base_api import basePage


class homePage(basePage):
    # pass
    _loginIcon = (By.ID, "a_login")

    def gotoLogin(self):
        from page.login_page import loginPage
        self.find(*self._loginIcon).click()
        return loginPage

    def gotoDetail(self, auction):
        self.enter(auction)