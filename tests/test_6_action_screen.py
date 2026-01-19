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
RED_T = ("xpath", "//a[@id='item_3_img_link']")
RED_ADD_TO_CART = ("xpath", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
sleep(1)


# def test_1():
#     wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
#     wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(data.PASSWORD)
#     wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
#     sleep(2)
#     action = ActionChains(driver)
#     action.click(driver.find_element(*RED_ADD_TO_CART)).perform()
#     sleep(2)
#     now_date = datetime.now().strftime('%H.%M.%S')
#     name_screen = "screenshot" + now_date + ".png"
#     driver.save_screenshot("C:\\Users\\14bas\\PycharmProjects\\pythonSelenium\\screen\\" + name_screen)
#     sleep(1)
#     driver.quit()

