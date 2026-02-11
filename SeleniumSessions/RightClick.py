import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

try:
    right_click_ele = driver.find_element(By.XPATH, ".//span[text()='right click me']")
    actionchains = ActionChains(driver)
    actionchains.context_click(right_click_ele).perform()
    context_options_ele = driver.find_elements(By.CSS_SELECTOR, "ul.context-menu-list li.context-menu-icon")
    for option in context_options_ele:
        if option.text.strip() == "Quit":
            option.click()
            break
    driver.switch_to.alert.accept()
finally:
    time.sleep(5)
    driver.quit()
