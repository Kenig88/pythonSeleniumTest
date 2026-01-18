from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.links import Links
import allure


class CartPage(BasePage):
    PAGE_URL = Links.CART_PAGE

    YOU_CART_LABEL = ("xpath", "//span[@class='title' and @data-test='title']")
    CARD_ITEM = ("xpath", "//div[@class='cart_item' and @data-test='inventory-item']")
    PRODUCTS_PAGE_BUTTON = ("xpath", "//button[@id='continue-shopping']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    BUTTON_REMOVE_BACKPACK = ("xpath", "//button[@id='remove-sauce-labs-backpack']")

    @allure.step("CartPage: check label text = '{expected}'")
    def check_label(self, expected: str = "Your Cart"):
        self.check_checkout_label(self.YOU_CART_LABEL, expected=expected)

    @allure.step("Check card item")
    def check_card_item(self):
        assert self.wait.until(EC.visibility_of_element_located(self.CARD_ITEM)).is_displayed()

    @allure.step("Transfer checkout page")
    def transfer_to_the_checkout_page(self):
        from pages.checkout_page import CheckoutPage
        self.continue_button(self.CHECKOUT_BUTTON, CheckoutPage)

    @allure.step("Transfer products page")
    def button_previous_products_page(self):
        from pages.products_page import ProductsPage
        self.previous_button(self.PRODUCTS_PAGE_BUTTON, ProductsPage)

    @allure.step("Remove items_from cart button")
    def remove_items_from_cart_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_REMOVE_BACKPACK)).click()
