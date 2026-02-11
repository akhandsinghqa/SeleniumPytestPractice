import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
try:
    best_sellers = driver.find_element(By.LINK_TEXT, "Bestsellers")
    driver.execute_script("arguments[0].click()", best_sellers)
    title = driver.execute_script("return document.title;")
    print(title)
    driver.execute_script("history.go(0);")
    # driver.execute_script("alert('hello akhand');")
    print(driver.execute_script("return document.documentElement.innerText;"))
    driver.execute_script("arguments[0].style.border = '3px solid red'",
                          driver.find_element(By.LINK_TEXT, "Bestsellers"))
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    back_to_top = driver.find_element(By.ID, "navBackToTop")
    driver.execute_script("arguments[0].scrollIntoView(true);", back_to_top)
    print(driver.execute_script("return navigator.userAgent;"))
    time.sleep(5)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    mobile = 'mobiles'
    driver.execute_script(f"document.getElementById('twotabsearchtextbox').value='{mobile}';")
finally:
    time.sleep(5)
    driver.close()
