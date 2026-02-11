import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

try:
    photo_manager = driver.find_element(By.ID, "Photo Manager")
    photo_manager.click()
    iframe = driver.find_element(By.XPATH, "(.//iframe[@class='demo-frame'])[1]")
    driver.switch_to.frame(iframe)
    from_this = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]")
    to_this = driver.find_element(By.ID, "trash")
    actions_chains = ActionChains(driver)
    actions_chains.drag_and_drop(from_this, to_this).perform()
    time.sleep(2)
    source_ele = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[2]")
    (actions_chains
     .click_and_hold(source_ele)
     .move_to_element(to_this)
     .release().perform())
    driver.switch_to.parent_frame()
finally:
    time.sleep(5)
    driver.quit()
