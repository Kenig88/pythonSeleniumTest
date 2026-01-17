from datetime import datetime
from selenium.webdriver import ActionChains
from config.data import Data as data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config.links import Links
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get(Links.LOGIN_PAGE)

USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//input[@id='login-button']")


def test_practice_site():
    sleep(2)
    # 1 регистрация
    wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
    wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(data.PASSWORD)
    wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
    sleep(1)

    # 2 проверка присутствия названия и цены рюкзака
    cart_product_1 = driver.find_element("xpath", "//a[@id='item_4_title_link']").text
    price_product_1 = driver.find_element("xpath", "(//div[@class='inventory_item_price'])[1]").text

    assert cart_product_1 == "Sauce Labs Backpack"
    assert price_product_1 == "$29.99"
    sleep(1)

    # 3 добавление в корзину
    add_to_cart = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    wait.until(EC.element_to_be_clickable(add_to_cart)).click()
    sleep(1)

    # 4 переход в корзину и проверка что рюкзак добавлен
    cart = driver.find_element("xpath", "//div[@id='shopping_cart_container']")
    wait.until(EC.element_to_be_clickable(cart)).click()
    assert cart_product_1 == "Sauce Labs Backpack"
    assert price_product_1 == "$29.99"
    sleep(1)

    # 5 переход на оформление заказа
    checkout = driver.find_element("xpath", "//button[@id='checkout']")
    wait.until(EC.element_to_be_clickable(checkout)).click()
    sleep(1)

    # 6 оформление заказа
    first_name = driver.find_element("xpath", "//input[@id='first-name']")
    last_name = driver.find_element("xpath", "//input[@id='last-name']")
    zip_code = driver.find_element("xpath", "//input[@id='postal-code']")
    button_continue = driver.find_element("xpath", "//input[@id='continue']")

    wait.until(EC.element_to_be_clickable(first_name)).send_keys(data.FIRST_NAME)
    wait.until(EC.element_to_be_clickable(last_name)).send_keys(data.LAST_NAME)
    wait.until(EC.element_to_be_clickable(zip_code)).send_keys(data.ZIP_CODE)
    wait.until(EC.element_to_be_clickable(button_continue)).click()
    sleep(1)

    # 8 проверка офомрления заказа
    tax = driver.find_element("xpath", "//div[@class='summary_tax_label']").text
    button_finish = driver.find_element("xpath", "//button[@id='finish']")

    assert cart_product_1 == "Sauce Labs Backpack"
    assert price_product_1 == "$29.99"
    assert tax == "Tax: $2.40"
    wait.until(EC.element_to_be_clickable(button_finish)).click()
    sleep(1)

    # 9 заказ оформлен и переход на главную страницу
    finish = driver.find_element("xpath", "//h2[text()='Thank you for your order!']").text
    button_back_home = driver.find_element("xpath", "//button[@id='back-to-products']")

    assert finish == "Thank you for your order!"
    wait.until(EC.element_to_be_clickable(button_back_home)).click()
    sleep(1)

    # 10
    header_to_main_page = driver.find_element("xpath", "//div[@class='header_label']").text
    assert header_to_main_page == "Swag Labs"
    sleep(1)
    driver.quit()
