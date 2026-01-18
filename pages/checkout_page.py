from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.links import Links
import allure


class CheckoutPage(BasePage):
    PAGE_URL = Links.CHECKOUT_PAGE

    CHECKOUT_LABEL = ("xpath", "//span[@class='title' and @data-test='title']")
    FIRST_NAME = ("xpath", "//input[@id='first-name']")
    LAST_NAME = ("xpath", "//input[@id='last-name']")
    ZIP_CODE = ("xpath", "//input[@id='postal-code']")
    BUTTON_CONTINUE = ("xpath", "//input[@id='continue']")
    BUTTON_CANCEL = ("xpath", "//button[@id='cancel']")

    @allure.step("CheckoutPage: check label text = '{expected}'")
    def check_label(self, expected: str = "Checkout: Your Information"):
        self.check_checkout_label(self.CHECKOUT_LABEL, expected=expected)

    @allure.step("Write first name")
    def write_first_name(self, first_name: str):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)).send_keys(first_name)

    @allure.step("Write last name")
    def write_last_name(self, last_name: str):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME)).send_keys(last_name)

    @allure.step("Write zip code")
    def write_zip_code(self, zip_code: str):
        self.wait.until(EC.element_to_be_clickable(self.ZIP_CODE)).send_keys(zip_code)

    @allure.step("Button continue")
    def transfer_to_the_checkout_overview_page(self):
        from pages.checkout_overview_page import CheckoutOverviewPage
        self.continue_button(self.BUTTON_CONTINUE, CheckoutOverviewPage)

    @allure.step("Button previous")
    def button_previous_from_cart_page(self):
        from pages.cart_page import CartPage
        self.previous_button(self.BUTTON_CANCEL, CartPage)
