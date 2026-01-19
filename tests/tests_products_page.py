from pages.products_page import ProductsPage

class TestProductsPage:

    def setup_method(self):
        self.products_page = ProductsPage(self.driver)

    # def test_products_page(self):
    #     self.products_page.open()
    #     self.products_page.check_products_label()
    #     self.products_page.check_price_product()
    #     self.products_page.check_cart_product_name()
    #     self.products_page.add_to_cart()