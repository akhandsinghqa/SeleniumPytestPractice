import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver


@pytest.fixture(scope="module")
def init_driver():
    print("------------ setup -----------------")
    options_fx = Options()
    options_fx.add_argument("--headless")
    global driver
    driver = webdriver.Firefox(options=options_fx)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://www.google.com/")

    yield
    print("----------- teardown -----------------")
    driver.quit()


# def test_google_title(init_driver):
#     assert driver.title == "Googleq"
#
#
# def test_google_url(init_driver):
#     assert driver.current_url == "https://www.google.com/"

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com/"
