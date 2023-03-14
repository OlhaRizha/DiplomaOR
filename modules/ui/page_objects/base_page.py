from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r'c:/Users/Lenovo/DiplomaOR/'
    DRIVER_NAME = 'chromedriver.exe'

    def __init__(self):
        """
        Initializes the Chrome driver with the specified path.
        """
        self.driver = webdriver.Chrome(service=Service(BasePage.PATH+BasePage.DRIVER_NAME))
        


    def close(self):
        """
        Closes the currently open Chrome browser window.
        """
        self.driver.close()