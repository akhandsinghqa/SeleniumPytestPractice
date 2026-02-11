from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# timeout =10
# dynamic wait
# important : wait will be applied for all the web element
# global wait
# it's only for web elements not handle title , url , alerts

driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("automation python")
driver.close()
