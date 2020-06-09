import time
from api.base_api import basePage
from selenium.webdriver.common.by import By
from page.home_page import homePage


class loginPage(basePage):
    _username = (By.ID, "loginId")
    _pwd = (By.ID, "password")
    _loginButton = (By.ID, "loginBtn")
    _logout = (By.LINK_TEXT, "退出")
    _loginIcon = (By.ID, "a_login")

    def loginByUsername(self, username, password):  # 登录框输入内容
        # 加*是为了解出值，否则find_element不支持
        # 等级登陆，进入登陆页面
        # self.find(*self._loginIcon).click()
        # 用户名
        self.send_keys(loc=self._username, keyword=username)
        # 密码
        self.send_keys(loc=self._pwd, keyword=password)
        self.find(*self._loginButton).click()
        time.sleep(3)
        return self


