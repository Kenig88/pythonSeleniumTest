from selenium.webdriver import Keys
from config.data import Data as data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config.links import Links
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get(Links.LOGIN_PAGE)

USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//input[@id='login-button']")
DROPDOWN_ELEMENT = ("xpath", "//select[@data-test='product-sort-container']")
sleep(1)


def test_1():
    wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
    wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(data.PASSWORD)
    wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
    sleep(2)
    DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
    DROPDOWN.select_by_index(1)
    sleep(2)

    sleep(2)
    driver.quit()

