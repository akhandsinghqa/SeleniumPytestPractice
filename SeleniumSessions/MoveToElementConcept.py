import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")

try:
    login_ele = driver.find_element(By.XPATH, ".//div[text()='Login']")
    add_ons = driver.find_element(By.XPATH, ".//div[text()='Add-ons']")
    actions_chains = ActionChains(driver)
    actions_chains.move_to_element(add_ons).perform()
    actions_chains.move_to_element(login_ele).perform()
    actions_chains.click().perform()

finally:
    time.sleep(5)
    driver.quit()
