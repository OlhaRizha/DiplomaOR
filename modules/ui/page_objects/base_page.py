from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Створення класу BasePage, що виконує базові операції для роботи з браузером Chrome, 
# ініціалізуючи його драйвер
class BasePage:
    PATH=r'c:/Users/Lenovo/DiplomaOR/'
    DRIVER_NAME='chromedriver.exe'

    def __init__(self):
        self.driver=webdriver.Chrome(service=Service(BasePage.PATH+BasePage.DRIVER_NAME))
        
    #Cтворення методу об'єкта, що перевіряє відповідність заголовку певної веб сторінки на GitHub
    #  та повертає результат цієї перевірки
    def check_title(self,expected_title):
        return self.driver.title==expected_title

    #Cтворення методу об'єкта класа, що відповідає за закриття відкритого браузера
    def close(self):
        self.driver.close()