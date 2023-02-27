from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

#Створення дочірнього класу SignUpPage(BasePage), на основі якого будуть створені тести 
# для перевірки веб сторінки Sign Up на сайті GitHub
class SignUpPage(BasePage):
    URL='https://github.com/signup'

    def __init__(self):
        super().__init__()

    #Створення методу об'єкта що відправляє запит GET на URL адресу
    def go_to(self):
        self.driver.get(SignUpPage.URL)

    #Створення методу об'єкта, що виконує ввід певних даних для реєстрації на GitHub,
    #  використовуючи електронну пошту вже зареєстрованого користувача
    def enter_email(self,email):
        regist_elem=self.driver.find_element(By.ID, "email")
        regist_elem.send_keys(email)
        
    #Cтворення методу об'єкта, що перевіряє наявність помилки під час введення 
    # електронної пошти вже існуючого користувача для виконання реєстрації на GitHub
    def check_error(self,expected_error):
        error_elem=self.driver.find_element(By.ID, "email-err")
        return error_elem==expected_error
    
    
    
    