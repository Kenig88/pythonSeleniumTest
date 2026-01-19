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
# driver.get(Links.RADIO_BUTTON)
# sleep(2)
#
# YES_RADIO = ("xpath", "//input[@id='yesRadio']")
# YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")
#
#
#
# # def test_1():
# #     wait.until(EC.element_to_be_clickable(YES_RADIO_LABEL)).click()
# #     assert driver.find_element(*YES_RADIO).is_selected() == True
# #
# #
# #     sleep(2)
# #     driver.quit()
