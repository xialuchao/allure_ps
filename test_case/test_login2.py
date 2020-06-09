import allure
import pytest

@allure.title("登录功能")  # 用例标题
@allure.feature("测试登录功能的类")  # 归为大类
class TestLogin2:
    # base_url = "http://ft1.home.zhaoonline.com/login.shtml?back=http%3A%2F%2Fft1.sh.zhaoonline.com%2F"
    login_message = [
        {"username": "1000333", "password": "admin123"},
        {"username": "1000222", "password": "admin123"},
    ]
    @allure.story("登录用例")  # 归为子类
    @allure.severity(allure.severity_level.CRITICAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize("login_message", login_message)
    def test_login2(self, common_browser, login_message):
        # 方法一：直接调用loginpage
        from page.login_page import loginPage
        # page = loginPage(common_browser)
        # page.loginByUsername(username=login_message['username'], password=login_message['password'])
        # assert "赵涌在线" in common_browser.title
        # 方法二：通过主页的登陆跳转到登陆页面进行登陆
        from page.home_page import homePage
        homePage(common_browser).gotoLogin()
        loginPage(common_browser).loginByUsername(username=login_message['username'], password=login_message['password'])
        # print(page.loginByUsername(username=login_message['username'], password=login_message['password']))
        # import time
        # time.sleep(2)
        # homePage(common_browser).gotoLogin().\
        #     loginByUsername(username=login_message['username'], password=login_message['password'])
        # issiue1: need self

        # homePage(common_browser).gotoLogin().loginByUsername(self, username=login_message['username'], password=login_message['password'])
        # common_browser.get(self.base_url)

        # page.gotoLogin().loginByUsername(self, username=login_message['username'], password=login_message['password'])

        # page.click_login()


if __name__ == '__main__':
    pytest.main()

