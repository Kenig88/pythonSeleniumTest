import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    # с этим методом все ок!
    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Open {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    # с этим методом все ок!
    def check_checkout_label(self, locator: tuple[str, str], expected: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        actual = el.text.strip()
        assert actual == expected, f"Текст не совпал. Ожидали: {expected!r}, получили: {actual!r}"

    # используется в ProductsPage
    def add_item_to_cart(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # используется в ProductsPage
    def check_products_price(self, locator: tuple[str, str], price: str):
        assert self.wait.until(EC.visibility_of_element_located(locator)).text == price, "Цена расходится!"

    def continue_button(self, locator: tuple[str, str], page):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return page(self.driver)

    def previous_button(self, locator: tuple[str, str], page):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return page(self.driver)

    #используется в checkout_overview_page
    def check_text(self, locator: tuple[str, str], assert_item: str):
        assert self.wait.until(EC.presence_of_element_located(locator)).text == assert_item


    # def make_screenshot(self, screenshot_name: str):
    #     allure.attach(
    #         body=self.driver.get_screenshot_as_png(),
    #         name=screenshot_name,
    #         attachment_type=AttachmentType.PNG
    #     )
