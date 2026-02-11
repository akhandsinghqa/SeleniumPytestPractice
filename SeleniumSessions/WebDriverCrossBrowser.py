import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = input("Enter the browser name : ").lower()
driver = None
if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
else:
    print("please enter the correct browser name:", browser)

driver.maximize_window()
driver.implicitly_wait(10)
try:
    driver.get("https://www.facebook.com/")

    assert driver.title == "Facebook – log in or sign up"

    driver.find_element(By.ID, "email").send_keys("admin123@demo.com")
    driver.find_element(By.ID, "pass").send_keys("password123")

    driver.find_element(By.CSS_SELECTOR, "[data-testid='royal-login-button']").click()

    error = driver.find_element(By.CSS_SELECTOR, "#email_container").text
    print("Error Message : ", error)
    assert "The email address you entered isn't connected to an account." in error
finally:
    time.sleep(5)
    driver.quit()
