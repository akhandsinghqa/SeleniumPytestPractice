import pytest


# @pytest.fixture(params=["firefox", "chrome"], scope='class')
# def init_driver(request):
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox()
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome()
#
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestGoogle(BaseTest):

    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.current_url == "https://www.google.com/"
