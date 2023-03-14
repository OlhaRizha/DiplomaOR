from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage(BasePage):
    """
    Child class of BasePage, used to test the Sign Up page on GitHub.
    """
    URL = 'https://github.com/signup'

    def __init__(self):
        super().__init__()

    def go_to(self):
        """
        Sends a GET request to the Sign Up page URL.
        """
        self.driver.get(SignUpPage.URL)

    def enter_email(self, email):
        """
        Enters an email for registration on GitHub, using an email that is already registered.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "email")))

        regist_elem = self.driver.find_element(By.ID, "email")
        regist_elem.send_keys(email)

    def check_error(self, expected_error):
        """
        Checks for the presence of an error during entry of an email that is already registered on GitHub.
        """
        error_elem = self.driver.find_element(By.ID, "email-err")
        return error_elem == expected_error
