import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options_ch = Options()
options_ch.add_argument("--headless")
driver = webdriver.Chrome(options=options_ch)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
print(driver.title)
try:
    pass
finally:
    time.sleep(5)
    driver.quit()
