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
DROPDOWN_ELEMENT = ("xpath", "//select[@data-test='product-sort-container']")
MENU = ("xpath", "//button[@id='react-burger-menu-btn']")
SIDEBAR_ABOUT = ("xpath", "//a[@id='about_sidebar_link']")

sleep(2)


# def test_1():
#     wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
#     wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(data.PASSWORD)
#     wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
#
#     wait.until(EC.element_to_be_clickable(MENU)).click()
#     wait.until(EC.element_to_be_clickable(SIDEBAR_ABOUT)).click()
#
#     sleep(2)
#     driver.quit()
