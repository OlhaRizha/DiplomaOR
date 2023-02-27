from modules.ui.page_objects.sign_up_page import SignUpPage
import pytest
import time

#Створення теста з міткою signup, що створює об'єкт класу SignUpPage,
# перевіряє можливість відкрити веб сторінку Sign Up сайту GitHub, 
# перевіряє можливість ввести електронну пошту вже існуючого користувача для здійснення реєстрації та
# перевіряє якою буде помилка у відповідь на цю дію,
# перевіряє чи назва даної сторінки така як очікується, закриває цю сторінку
@pytest.mark.signup
def test_check_incorrect_data_for_sign_up_page():
    sign_up_page=SignUpPage()

    sign_up_page.go_to()

    time.sleep(2)

    sign_up_page.enter_email("olharizha@gmail.com")

    sign_up_page.check_error("Email is invalid or already taken")


    sign_up_page.close()