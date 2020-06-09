from selenium.webdriver.common.by import By
from api.base_api import basePage
from page.home_page import homePage


class detailPage(basePage):
    _bid_button = (By.ID, "_btn_xiangqing_bid")

    def bid_auction(self,auction):
        self.enter(auction)
        self.find(*self._bid_button).click()
