import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    # driver : WebDriver
    pass


class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
        "username,password",
        [
            ("admin@gmail.com", "admin123"),
            ("akhand@gmail.com", "akhand123")
        ]
    )
    def test_login(self, username, password):
        self.driver.delete_all_cookies()
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.XPATH, ".//button[@data-test-id='email-submit-button']").click()
        self.driver.find_element(By.ID, "passwordBtn").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginBtn").click()
        warning = str(
            self.driver.find_element(By.XPATH, ".//div[@data-test-id='error-alert-PASSWORD_DEPRECATED']").text)
        assert "Your password has been invalidated." in warning
