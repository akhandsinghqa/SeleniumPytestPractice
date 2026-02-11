import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.reddit.com/")
try:
    cookies = driver.get_cookies()
    print(cookies)
    for cook in cookies:
        print(cook)
    driver.add_cookie({"name": "new", "domain": "reddit.com", "value": "python"})
    print(driver.get_cookies())
finally:
    time.sleep(5)
    driver.quit()
