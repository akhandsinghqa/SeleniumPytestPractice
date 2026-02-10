import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver


@pytest.fixture(scope='class')
def init_ff_driver(request):
    options_ff = FirefoxOptions()
    options_ff.add_argument("--headless")
    ff_driver = webdriver.Firefox(options=options_ff)
    request.cls.driver = ff_driver
    yield
    ff_driver.quit()


@pytest.fixture(scope='class')
def init_ch_driver(request):
    options_ch = ChromeOptions()
    options_ch.add_argument("--headless")
    ch_driver = webdriver.Chrome(options=options_ch)
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()


@pytest.mark.usefixtures("init_ff_driver")
class BaseFirefoxTest:
    driver = FirefoxDriver


class TestMozillaFirefox(BaseFirefoxTest):

    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"


@pytest.mark.usefixtures("init_ch_driver")
class BaseChromeTest:
    driver = ChromeDriver


class TestGoogleChrome(BaseChromeTest):

    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"
