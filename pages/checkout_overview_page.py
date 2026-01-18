from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.links import Links
import allure


class CheckoutOverviewPage(BasePage):
    PAGE_URL = Links.CHECKOUT_OVERVIEW_PAGE

    CHECKOUT_OVERVIEW_LABEL = ("xpath", "//span[@class='title' and @data-test='title']")
    CARD_ITEM = ("xpath", "//div[@class='cart_item']")
    BUTTON_CANCEL = ("xpath", "//button[@id='cancel']")
    BUTTON_CONTINUE = ("xpath", "//button[@id='finish']")
    PAYMENT_INFORMATION = ("xpath", "(//div[@class='summary_value_label'])[1]")
    SHIPPING_INFORMATION = ("xpath", "(//div[@class='summary_value_label'])[2]")
    SUBTOTAL_PRICE = ("xpath", "//div[@class='summary_subtotal_label']")
    TAX_PRICE = ("xpath", "//div[@class='summary_tax_label']")
    TOTAL_PRICE = ("xpath", "//div[@class='summary_total_label']")

    @allure.step("CheckoutOverviewPage: check label text = '{expected}'")
    def check_label(self, expected: str = "Checkout: Overview"):
        self.check_checkout_label(self.CHECKOUT_OVERVIEW_LABEL, expected=expected)

    @allure.step
    def check_card_item(self):
        assert self.wait.until(EC.presence_of_element_located(self.CARD_ITEM)).is_displayed()

    @allure.step("Check payment information")
    def check_payment_information(self, text_info):
        self.check_text(self.PAYMENT_INFORMATION, text_info)
        # assert self.wait.until(EC.presence_of_element_located(self.PAYMENT_INFORMATION)).text == text_info

    @allure.step("Check shipping information")
    def check_shipping_information(self, post_service):
        self.check_text(self.SHIPPING_INFORMATION, post_service)
        # assert self.wait.until(EC.presence_of_element_located(self.SHIPPING_INFORMATION)).text == post_service

    @allure.step("Subtotal price")
    def check_subtotal_price(self, price):
        self.check_text(self.SUBTOTAL_PRICE, price)
        # assert self.wait.until(EC.presence_of_element_located(self.SUBTOTAL_PRICE)).text == price

    @allure.step("Check tax price")
    def check_tax_price(self, tax_price):
        self.check_text(self.TAX_PRICE, tax_price)

        # assert self.wait.until(EC.presence_of_element_located(self.TAX_PRICE)).text == tax_price

    @allure.step("Check total price")
    def check_total_price(self, total_price):
        self.check_text(self.TOTAL_PRICE, total_price)
        # assert self.wait.until(EC.presence_of_element_located(self.TOTAL_PRICE)).text == total_price

    @allure.step("Finish button")
    def transfer_checkout_complete_page(self):
        from pages.checkout_complete_page import CheckoutCompletePage
        self.continue_button(self.BUTTON_CONTINUE, CheckoutCompletePage)

    @allure.step("Cancel button")
    def cancel_button(self):
        from pages.products_page import ProductsPage
        self.previous_button(self.BUTTON_CANCEL, ProductsPage)
