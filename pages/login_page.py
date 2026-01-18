from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.links import Links
import allure


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON = ("xpath", "//input[@id='login-button']")

    @allure.step("Enter login")
    def enter_login(self, login: str):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password: str):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        from pages.products_page import ProductsPage
        return ProductsPage(self.driver)

    @allure.step("Check home url")
    def check_home_url(self):
        assert self.wait.until(EC.url_to_be(Links.HOST))
