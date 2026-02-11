import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
try:
    driver.find_element(By.NAME,"upfile").send_keys("")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
finally:
    time.sleep(5)
    driver.quit()
