import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")

try:
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login = driver.find_element(By.XPATH, "//input[@value='Login']")
    action_chain = ActionChains(driver)
    (action_chain.send_keys_to_element(username, "admin123")
     .send_keys_to_element(password, "password123")
     .click(login).perform())

finally:
    time.sleep(5)
    driver.quit()
