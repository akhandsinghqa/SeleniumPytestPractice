from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 5)
try:
    # wait.until(EC.title_is("Facebook – log in or sign up"))
    wait.until(EC.title_contains("Facebook"))
    print(driver.title)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "email")))
    search_box.send_keys("automation python")
    driver.find_element(By.ID, "pass").send_keys("password")
finally:
    driver.close()
