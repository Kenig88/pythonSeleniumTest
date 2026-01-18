from pages.login_page import LoginPage
from config.data import Data


class TestLoginPage:
    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_submit_button()
