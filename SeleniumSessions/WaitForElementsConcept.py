from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.freshworks.com/")
wait = WebDriverWait(driver, 5)
try:
    footer_link = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "footer ul li")))
    print(len(footer_link))
    for link in footer_link:
        print(link.text)
finally:
    driver.close()
