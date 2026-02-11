import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
try:
    driver.find_element(By.LINK_TEXT, "Mobiles").click()
    driver.back()
    driver.forward()
    driver.back()
    driver.refresh()
finally:
    time.sleep(5)
    driver.quit()
