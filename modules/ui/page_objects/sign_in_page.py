from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

#Створення дочірнього класу SignInPage(BasePage), на основі якого будуть створені тести 
# для перевірки веб сторінки Sign In на сайті GitHub
class SignInPage(BasePage):
    URL='https://github.com/login'

    def __init__(self):
        super().__init__()

#Створення методу об'єкта що відправляє запит GET на URL адресу
    def go_to(self):
        self.driver.get(SignInPage.URL)

#Створення методу об'єкта, що виконує ввід певних даних для виконання входу на GitHub
    def try_login(self,username,password):
        login_elem=self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)
        pass_elem=self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        btn_elem=self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

#Cтворення методу об'єкта, що перевіряє відповідність заголовку певної веб сторінки на GitHub
#  та повертає результат цієї перевірки
    def check_title(self,expected_title):
        return self.driver.title==expected_title