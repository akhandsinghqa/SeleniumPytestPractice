from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
wait = WebDriverWait(driver, 5)
try:
    driver.find_element(By.NAME, "proceed").click()
    alert = wait.until(EC.alert_is_present())
    print(alert.text)
    alert.accept()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".forgot-link"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "next"))).click()
    alert = wait.until(EC.alert_is_present())
    print(alert.text)
    alert.accept()
finally:
    driver.close()
