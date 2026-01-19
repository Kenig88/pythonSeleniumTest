# from datetime import datetime
# from selenium.webdriver import ActionChains
# from config.data import Data as data
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# from config.links import Links
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.page_load_strategy = "eager"
# driver = webdriver.Chrome(options=options)
#
# wait = WebDriverWait(driver, 15, poll_frequency=1)
#
# driver.get(Links.BUTTONS)
# sleep(2)
#
# one = driver.find_element("xpath", "//button[text()='Click Me']")
# double = driver.find_element("xpath", "//button[@id='doubleClickBtn']")
# right = driver.find_element("xpath", "//button[@id='rightClickBtn']")
#
#
# # def test_1():
# #     action = ActionChains(driver)
# #     action.double_click(double).context_click(right).click(one).perform()
# #
# #     sleep(2)
# #     driver.quit()
