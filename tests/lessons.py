# from config.data import Data as data
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# from config.links import Links
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 15, poll_frequency=1)
#
# driver.get(Links.LOGIN_PAGE)
#
# USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//input[@id='login-button']")
#
# sleep(1)
# wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(data.LOGIN)
# sleep(1)
# wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(data.PASSWORD)
# sleep(1)
# wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
# sleep(1)
#
#
#
