import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.orangehrm.com/en/30-day-free-trial")

print(driver.title)
try:
    username_elem = driver.find_element(By.NAME, "subdomain")
    name_elem = driver.find_element(By.ID, "Form_getForm_Name")
    # email_elem = driver.find_element(By.CSS_SELECTOR, "input.email.text")
    email_alt = driver.find_element(By.XPATH, ".//input[@class='email text']")
    contact_elem = driver.find_element(By.XPATH, ".//input[@type='tel']")
    country_elem = driver.find_element(By.ID, "Form_getForm_Country")
    submit_elem = driver.find_element(By.ID, "Form_getForm_action_submitForm")
    solutions_elem = driver.find_element(By.LINK_TEXT, "Solutions")
    total_link = driver.find_elements(By.TAG_NAME, "a")
    image_link = driver.find_elements(By.TAG_NAME, "img")

    username_elem.send_keys("admin12345")
    name_elem.send_keys("onlyadmin")
    # email_elem.send_keys("admin123@demo.com")
    email_alt.send_keys("admin123@demo.com")
    contact_elem.send_keys("1234567890")

    print(len(total_link))
    for link in total_link:
        if link.get_attribute("href") != "":
            print(link.text)
            print(link.get_attribute("href"))

    print(len(image_link))
    for image in image_link:
        print(image.get_attribute("src"))

    solutions_elem.click()
finally:
    time.sleep(5)
    driver.quit()
