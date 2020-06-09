import allure
import pytest
from page.home_page import homePage

@allure.title("出价用例")  # 用例标题
class TestBid:
    @allure.story("出价用例")  # 归为子类

    def test_bid(self, common_browser):
        from page.detail_page import detailPage
        from page.login_page import loginPage
        homePage(common_browser).gotoLogin()
        loginPage(common_browser).loginByUsername(1000222, "admin123")
        detailPage(common_browser).bid_auction("3827674")

if __name__ == '__main__':
    pytest.main()

