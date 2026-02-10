from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options_fx = Options()
options_fx.add_argument("--headless")


def test_google():
    driver = webdriver.Firefox(options=options_fx)
    try:
        driver.implicitly_wait(10)
        driver.get("https://www.google.com/")
        assert driver.title == "Google"
    finally:
        driver.quit()


def test_facebook():
    driver = webdriver.Firefox(options=options_fx)
    try:
        driver.implicitly_wait(10)
        driver.get("https://www.facebook.com/")
        assert driver.title == "Facebook – log in or sign up"
    finally:
        driver.quit()


def test_linkedin():
    driver = webdriver.Firefox(options=options_fx)
    try:
        driver.implicitly_wait(10)
        driver.get("https://www.linkedin.com")
        assert driver.title == "LinkedIn: Log In or Sign Up"
    finally:
        driver.quit()


def test_gmail():
    driver = webdriver.Firefox(options=options_fx)
    try:
        driver.implicitly_wait(10)
        driver.get("https://www.gmail.com")
        assert driver.title == "Gmail"
    finally:
        driver.quit()


def test_rediff():
    driver = webdriver.Firefox(options=options_fx)
    try:
        driver.implicitly_wait(10)
        driver.get("https://www.rediff.com")
        assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Rediff Gurus"
    finally:
        driver.quit()
