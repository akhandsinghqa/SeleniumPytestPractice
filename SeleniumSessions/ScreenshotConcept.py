import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options_ch = Options()
options_ch.add_argument("--headless")
driver = webdriver.Chrome(options=options_ch)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
# driver.get_screenshot_as_file("reddit.png")

# full screenshot in headless mode
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot("reddit_full.png")
try:
    pass
finally:
    time.sleep(5)
    driver.quit()
