import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

try:
    sign_in = driver.find_element(By.CSS_SELECTOR, ".signin-btn")
    sign_in.click()
    popup = driver.switch_to.alert
    message = popup.text
    print(message)
    popup.accept()
    driver.switch_to.default_content()
finally:
    time.sleep(5)
    driver.quit()
