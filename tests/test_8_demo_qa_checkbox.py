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
# driver.get(Links.CHECK_BOX)
#
# CHECKBOX_HOME = ("xpath", "//input[@id='tree-node-home']")
# CHECKBOX_HOME_SPAN = ("xpath", "//span[text()='Home']")
#
# sleep(2)
#
#
# # def test_1():
# #     wait.until(EC.element_to_be_clickable(CHECKBOX_HOME_SPAN)).click()
# #     assert driver.find_element(*CHECKBOX_HOME).is_selected()
# #
# #     sleep(2)
# #     driver.quit()
