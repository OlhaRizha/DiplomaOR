from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

#Створення дочірнього класу SignUpPage(BasePage), на основі якого будуть створені тести 
# для перевірки веб сторінки Реєстрація на сайті Rozetka
class SignUpRozetka(BasePage):
    URL='https://rozetka.com.ua/ua'

    def __init__(self):
        super().__init__()

    #Створення методу об'єкта що відправляє запит GET на URL адресу
    def go_to(self):
        self.driver.get(SignUpRozetka.URL)

    #Створення методу об'єкта, що відповідає за відкриття вікна для реєстрації нового користувача
    def open_registration_window(self):
        btn_user=self.driver.find_element(By.XPATH, '//rz-user/button')
        btn_user.click()
        time.sleep(2)
      
        btn_regis=self.driver.find_element(By.XPATH, '//fieldset/div[5]/button[2]')
       
        btn_regis.click()
       

    #Створення методу об'єкта, що виконує ввід імені в поле "Ім'я" для реєстрації нового користувача на Rozetka
    def enter_name(self,name):
        regis_elem1=self.driver.find_element(By.ID, "registerUserName")
        regis_elem1.send_keys(name)
      

    #Створення методу об'єкта для перевірки наявності помилки під час введення некоректного імені в поле "Ім'я"
    def assert_error_name(self,error_name):
        error_elem1=self.driver.find_element(By.XPATH, '//div[1]/form-error/p')
        return error_elem1==error_name
        

    #Метод об'єкта для видалення введених некоректних даних в полі "Ім'я"   
    def clear_name(self):
        remove_elem1=self.driver.find_element(By.ID, "registerUserName")
        remove_elem1.clear()
        


    #Метод об'єкта для введення даних в поле "Прізвище"
    def enter_second_name(self,second_name):
        regis_elem2=self.driver.find_element(By.ID, "registerUserSurname")
        regis_elem2.send_keys(second_name)
        

    #Метод для перевірки наявності помилки під час введення некоректних даних в поле "Прізвище"
    def assert_error_second_name(self,error_second_name):
        error_elem2=self.driver.find_element(By.XPATH, "//fieldset/div[2]/form-error/p")
        return error_elem2==error_second_name
        

    #Метод об'єкта для видалення некоректних даних в полі "Прізвище"   
    def clear_second_name(self):
        remove_elem2=self.driver.find_element(By.ID, "registerUserSurname")
        remove_elem2.clear()
        


    #Метод об'єкта для введення даних в поле "Номер телефону"   
    def enter_phone_number(self,number):
        regis_elem3=self.driver.find_element(By.ID, "registerUserPhone")
        regis_elem3.send_keys(number)
        

    #Метод об'єкта для перевірки наявності помилки під час введення некоректних даних в поле "Номер телефону"
    def assert_error_phone_number(self,error_phone_number):
        error_elem3=self.driver.find_element(By.XPATH, "//fieldset/div[3]/form-error/p")
        return error_elem3==error_phone_number
        

    #Метод об'єкта для видалення некоректних даних в полі "Номер телефону"
    def clear_phone_number(self):
        remove_elem3=self.driver.find_element(By.ID, "registerUserPhone")
        remove_elem3.clear()
        


    #Метод об'єкта для введення даних в поле "Ел.пошта"
    def enter_email(self,email):
        regis_elem4=self.driver.find_element(By.ID, "registerUserEmail")
        regis_elem4.send_keys(email)
        

    #Метод для перевірки наявності помилки під час введення некоректних даних в поле "Ел.пошта"
    def assert_error_email(self,error_email):
        error_elem4=self.driver.find_element(By.XPATH, "//fieldset/div[4]/form-error/p")
        return error_elem4==error_email
        

    #Метод об'єкта для видалення некоректних даних в полі "Ел.пошта"   
    def clear_email(self):
        remove_elem4=self.driver.find_element(By.ID, "registerUserEmail")
        remove_elem4.clear()
        


    #Метод об'єкта для введення даних в поле "Придумайте пароль"
    def enter_password(self,password):
        regis_elem5=self.driver.find_element(By.ID, "registerUserPassword")
        regis_elem5.send_keys(password)
        

    #Метод для перевірки наявності помилки під час введення некоректних даних в поле "Придумайте пароль"
    def assert_error_password(self,error_password):
        error_elem5=self.driver.find_element(By.XPATH, "//div[5]/p/form-error/ul/li[3]/p")
        return error_elem5==error_password
        

    #Метод об'єкта для видалення некоректних даних в полі "Придумайте пароль"   
    def clear_password(self):
        remove_elem5=self.driver.find_element(By.ID, "registerUserPassword")
        remove_elem5.clear()
        
        
