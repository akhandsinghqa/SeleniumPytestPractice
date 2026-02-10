from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver


def setup_module():
    options_fx = Options()
    options_fx.add_argument("--headless")
    global driver
    driver = webdriver.Firefox(options=options_fx)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://www.google.com/")


def teardown_module():
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "https://www.google.com/"
