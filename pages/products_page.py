from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.links import Links
import allure


class ProductsPage(BasePage):
    PAGE_URL = Links.PRODUCTS_PAGE

    PRODUCTS_LABEL = ("xpath", "//span[@class='title' and @data-test='title']")
    CHECK_CARD_PRODUCT_NAME_BACKPACK = ("xpath", "//a[@id='item_4_title_link']")
    CHECK_PRICE_BACKPACK = ("xpath", "(//div[@class='inventory_item_price'])[1]")
    BACKPACK_ADD_TO_CART = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    BUTTON_CART = ("xpath", "//div[@id='shopping_cart_container']")

    @allure.step("ProductsPage: check label text = '{expected}'")
    def check_label(self, expected: str = "Products"):
        self.check_checkout_label(self.PRODUCTS_LABEL, expected=expected)

    # @allure.step("Check products logo")
    # def check_products_label(self):
    #     assert self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_LABEL)).text == "Products"

    @allure.step("Check cart product")
    def check_cart_product_name(self, text: str):
        cart_product = self.wait.until(EC.visibility_of_element_located(self.CHECK_CARD_PRODUCT_NAME_BACKPACK))
        assert cart_product.text == text

    @allure.step("Check price product")
    def check_price_backpack(self, price: str):
        self.check_products_price(self.CHECK_PRICE_BACKPACK, price)

    @allure.step("Add backpack from cart ")
    def backpack_add_to_cart(self):
        self.add_item_to_cart(self.BACKPACK_ADD_TO_CART)

    @allure.step("Transfer to the shopping cart")
    def transfer_to_the_shopping_cart_page(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CART)).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)
