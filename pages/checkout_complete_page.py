from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.links import Links
import allure


class CheckoutCompletePage(BasePage):
    PAGE_URL = Links.CHECKOUT_COMPLETE_PAGE

    CHECKOUT_COMPLETE_LABEL = ("xpath", "//span[@data-test='title']")
    COMPLETE_HEADER = ("xpath", "//h2[@class='complete-header']")
    COMPLETE_DESCRIPTION = ("xpath", "//div[@class='complete-text']")
    BUTTON_BACK_TO_PRODUCTS = ("xpath", "//button[@id='back-to-products']")

    @allure.step("CheckoutCompletePage: check label text = '{expected}'")
    def check_label(self, expected: str = "Checkout: Complete!"):
        self.check_checkout_label(self.CHECKOUT_COMPLETE_LABEL, expected=expected)

    @allure.step("Check complete header")
    def check_complete_header(self):
        assert self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)), "Хедер отсутствует!"

    @allure.step("Check complete description")
    def check_complete_description(self):
        assert self.wait.until(EC.visibility_of_element_located(self.COMPLETE_DESCRIPTION)), "Описание отсутствует!"

    @allure.step("Click 'Back to home'")
    def click_back_to_products_page(self):
        from pages.products_page import ProductsPage
        self.previous_button(self.BUTTON_BACK_TO_PRODUCTS, ProductsPage)

    # @allure.step("Check checkout complete label: '{expected}'")
    # def check_checkout_complete_label(self, expected="Checkout: Complete!"):
    #     assert self.wait.until(
    #         EC.text_to_be_present_in_element(self.CHECKOUT_COMPLETE_LABEL, expected)
    #     ), f"Лейбл не найден или текст не совпал. Ожидали: {expected}"
