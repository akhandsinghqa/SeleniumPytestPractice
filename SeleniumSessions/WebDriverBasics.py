import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

assert driver.title == "Google", "Title is not Google"

driver.find_element(By.NAME, "q").send_keys("naveen automationlabs")
search_options_list = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li")
print("Length of the list : ",len(search_options_list))

for elem in search_options_list:
    print(elem.text)
    if elem.text == "naveen automationlabs playwright":
        elem.click()
        break

time.sleep(5)
driver.quit()
