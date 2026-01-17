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
WARRING = ("xpath", "//h3[text()='Epic sadface: Username and password do not match any user in this service']")

sleep(1)


def test_1():
    wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
    wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys("ds")
    wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
    sleep(2)
    assert driver.find_element(*WARRING).is_displayed()
    # wait.until(EC.text_to_be_present_in_element_value(*WARRING))
    driver.quit()
