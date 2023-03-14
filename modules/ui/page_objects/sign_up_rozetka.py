from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SignUpRozetka(BasePage):
    """
    Child class of BasePage, used to test the Sign Up page on Rozetka.com.ua
    """
    URL = 'https://rozetka.com.ua/ua'

    def __init__(self):
        super().__init__()

    def go_to(self):
        """
        Navigate to the registration page.
        """
        self.driver.get(SignUpRozetka.URL)

    def open_registration_window(self):
        """
        Open the registration window by clicking on the 'User' button, and then on the 'Registration' button.
        """
        btn_user = self.driver.find_element(By.XPATH, '//rz-user/button')
        btn_user.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//fieldset/div[5]/button[2]")))

        btn_regis = self.driver.find_element(
            By.XPATH, '//fieldset/div[5]/button[2]')
        btn_regis.click()

    def enter_name(self, name):
        """
        Enter a user's name in the 'Name' field.
        """
        regis_elem1 = self.driver.find_element(By.ID, "registerUserName")
        regis_elem1.send_keys(name)

    def assert_error_name(self):
        """
        Assert that the error message for entering an incorrect name is displayed.
        """
        error_elem1 = self.driver.find_element(
            By.XPATH, '//div[1]/form-error/p')
        assert error_elem1.text == "Введіть своє ім'я кирилицею"

    def clear_name(self):
        """
        Clear the contents of the 'Name' field.
        """
        remove_elem1 = self.driver.find_element(By.ID, "registerUserName")
        remove_elem1.clear()

    def enter_second_name(self, second_name):
        """
        Enter a user's second name in the 'Surname' field.
        """
        regis_elem2 = self.driver.find_element(By.ID, "registerUserSurname")
        regis_elem2.send_keys(second_name)

    def assert_error_second_name(self):
        """
        Assert that the error message for entering an incorrect second name is displayed.
        """
        error_elem2 = self.driver.find_element(
            By.XPATH, "//fieldset/div[2]/form-error/p")
        assert error_elem2.text == "Введіть своє прізвище кирилицею"

    def clear_second_name(self):
        """
        Clear the contents of the 'Surname' field.
        """
        remove_elem2 = self.driver.find_element(By.ID, "registerUserSurname")
        remove_elem2.clear()

    def enter_phone_number(self, number):
        """
        Enter a user's phone number in the 'Phone number' field.
        """
        regis_elem3 = self.driver.find_element(By.ID, "registerUserPhone")
        regis_elem3.send_keys(number)

    def assert_error_phone_number(self):
        """
        Assert that the error message for entering an incorrect phone number is displayed.
        """
        error_elem3 = self.driver.find_element(
            By.XPATH, "//fieldset/div[3]/form-error/p")
        assert error_elem3.text == "Введіть номер мобільного телефону"

    def clear_phone_number(self):
        """
        Clear the phone number field.
        """
        remove_elem3 = self.driver.find_element(By.ID, "registerUserPhone")
        remove_elem3.clear()

    def enter_email(self, email):
        """
        Enter the email in the email field.
        """
        regis_elem4 = self.driver.find_element(By.ID, "registerUserEmail")
        regis_elem4.send_keys(email)

    def assert_error_email(self):
        """
        Assert that the error message for entering an incorrect email is displayed.
        """
        error_elem4 = self.driver.find_element(
            By.XPATH, "//fieldset/div[4]/form-error/p")
        assert error_elem4.text == "Введіть свою ел. пошту"

    def clear_email(self):
        """
        Clear the email field of incorrect data.
        """
        remove_elem4 = self.driver.find_element(By.ID, "registerUserEmail")
        remove_elem4.clear()

    def enter_password(self, password):
        """
        Enter the password in the password field.
        """
        regis_elem5 = self.driver.find_element(By.ID, "registerUserPassword")
        regis_elem5.send_keys(password)

    def assert_error_password(self):
        """
        Assert that the error message for entering an incorrect password is displayed.
        """
        error_elem5 = self.driver.find_element(
            By.XPATH, "//div[5]/p/form-error/ul/li[3]/p")
        assert error_elem5.text == "Не менше 6 символів"

    def clear_password(self):
        """
        Clear the password field of incorrect data.
        """
        remove_elem5 = self.driver.find_element(By.ID, "registerUserPassword")
        remove_elem5.clear()
