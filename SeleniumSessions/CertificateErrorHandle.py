import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options_ch = Options()
# options_ch.add_argument("--allow-running-insecure-content")
# options_ch.add_argument("--ignore-certificate-errors")
options_ch.set_capability('acceptInsecureCerts', True)
driver = webdriver.Chrome(options=options_ch)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
try:
    pass
finally:
    time.sleep(5)
    driver.close()
