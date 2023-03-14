from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    """
    A class representing the Sign In page on GitHub website.

    Inherits from the BasePage class and adds methods to interact with the Sign In page.
    """
    URL = 'https://github.com/login'

    def __init__(self):
        """
        Initializes an instance of the SignInPage class.

        Calls the constructor of the BasePage class to initialize the driver.
        """
        super().__init__()

    def go_to(self):
        """
        Navigates to the Sign In page by sending a GET request to its URL.
        """
        self.driver.get(SignInPage.URL)

    def check_title(self, expected_title):
        """
        Checks if the title of the current page matches the expected title.

        :param expected_title: The expected title of the page.
        :return: True if the title matches, False otherwise.
        """
        return self.driver.title == expected_title

    def try_login(self, username, password):
        """
        Attempts to log in to GitHub with the specified credentials.

        :param username: The username to log in with.
        :param password: The password to log in with.
        """
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()
