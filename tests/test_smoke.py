from tests.base_test import BaseTest
from time import sleep
import pytest
import allure



@allure.feature("Smoke test")
class TestSmoke(BaseTest):

    @allure.title("Simulated purchase")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_system(self):
        # loginPage
        self.loginPage.open()
        self.loginPage.check_home_url()
        self.loginPage.enter_login(self.data.LOGIN)
        self.loginPage.enter_password(self.data.PASSWORD)
        self.loginPage.click_submit_button()

        # productsPage
        self.productsPage.check_label()
        self.productsPage.backpack_add_to_cart()
        self.productsPage.transfer_to_the_shopping_cart_page()

        # cartPage
        self.cartPage.check_label()
        self.cartPage.check_card_item()
        self.cartPage.transfer_to_the_checkout_page()

        # checkoutPage
        self.checkoutPage.check_label()
        self.checkoutPage.write_first_name(self.data.FIRST_NAME)
        self.checkoutPage.write_last_name(self.data.LAST_NAME)
        self.checkoutPage.write_zip_code(self.data.ZIP_CODE)
        self.checkoutPage.transfer_to_the_checkout_overview_page()

        # checkout:Overview
        self.checkoutOverviewPage.check_label()
        self.checkoutOverviewPage.check_card_item()
        self.checkoutOverviewPage.transfer_checkout_complete_page()

        # checkoutCompletePage
        self.checkoutCompletePage.check_label()
        self.checkoutCompletePage.check_complete_header()
        self.checkoutCompletePage.check_complete_description()
        self.checkoutCompletePage.click_back_to_products_page()

        sleep(1)
