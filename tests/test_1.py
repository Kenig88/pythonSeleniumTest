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
TEXT_PRODUCTS = ("xpath", "//span[text()='Products']")

sleep(1)


def test_1():
    wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
    wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(data.PASSWORD)
    wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
    sleep(2)
    assert driver.find_element(*TEXT_PRODUCTS).text == "Products", "Хэдэр не сходится"
    url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == url, "URL не сходятся"
    driver.quit()
