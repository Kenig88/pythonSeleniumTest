from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from config.data import Data
import pytest


@pytest.mark.usefixtures("driver")
class BaseTest:
    data: Data
    loginPage: LoginPage
    productsPage: ProductsPage
    cartPage: CartPage

    @pytest.fixture(autouse=True)
    def setup_pages(self, request, driver):
        self.driver = driver
        self.data = Data()

        self.loginPage = LoginPage(self.driver)
        self.productsPage = ProductsPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutOverviewPage = CheckoutOverviewPage(self.driver)
        self.checkoutCompletePage = CheckoutCompletePage(self.driver)
