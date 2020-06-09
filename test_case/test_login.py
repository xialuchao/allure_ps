import allure
import pytest

@allure.title("登录功能")  # 用例标题
@allure.feature("测试登录功能的类")  # 归为大类
class TestLogin:
    login_message = [
        {"username": "1000666", "password": "admin123"},
        {"username": "1000111", "password": "admin123"},
    ]

    @allure.story("登录用例")  # 归为子类
    @allure.severity(allure.severity_level.CRITICAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize("login_message", login_message)
    def test_login(self, common_browser, login_message):
        from page.login_page import loginPage
        # 方法二：通过主页的登陆跳转到登陆页面进行登陆
        from page.home_page import homePage
        homePage(common_browser).gotoLogin()
        loginPage(common_browser).loginByUsername(username=login_message['username'], password=login_message['password'])
if __name__ == '__main__':
    pytest.main()

