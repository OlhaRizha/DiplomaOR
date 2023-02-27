from modules.ui.page_objects.sign_up_rozetka import SignUpRozetka
import pytest
import time

#Створення теста з міткою rozetka, що створює об'єкт класу SignUpPage,
# перевіряє можливість відкрити веб сторінку Реєстрації сайту Rozetka.com.ua, 
# перевіряє можливість ввести некоректні дані для здійснення реєстрації та
# перевіряє якою буде помилка у відповідь на цю дію

@pytest.mark.rozetka
def test_check_signup_name():
    sign_up_rozetka=SignUpRozetka()

    sign_up_rozetka.go_to()

    sign_up_rozetka.open_registration_window()

    #Перевірка поля "Ім'я"
    sign_up_rozetka.enter_name("12345")
    sign_up_rozetka.assert_error_name("Введіть своє ім'я кирилицею")
    sign_up_rozetka.clear_name()
   
    sign_up_rozetka.enter_name("%&*")
    sign_up_rozetka.assert_error_name("Введіть своє ім'я кирилицею")
    sign_up_rozetka.clear_name()

    sign_up_rozetka.enter_name("username")
    sign_up_rozetka.assert_error_name("Введіть своє ім'я кирилицею")
    
   
    #Перевірка поля "Прізвище"
    sign_up_rozetka.enter_second_name("6578")
    sign_up_rozetka.assert_error_second_name("Введіть своє прізвище кирилицею")
    sign_up_rozetka.clear_second_name()
   
    sign_up_rozetka.enter_second_name("#$@")
    sign_up_rozetka.assert_error_second_name("Введіть своє прізвище кирилицею")
    sign_up_rozetka.clear_second_name()

    sign_up_rozetka.enter_second_name("secondname")
    sign_up_rozetka.assert_error_second_name("Введіть своє прізвище кирилицею")
    
  
    #Перевірка поля "Номер телефону"
    sign_up_rozetka.enter_phone_number("1111111111")
    sign_up_rozetka.assert_error_phone_number("Введіть номер мобільного телефону")


    #Перевірка поля "Ел.пошта"
    sign_up_rozetka.enter_email("123")
    sign_up_rozetka.assert_error_email("Введіть номер мобільного телефону")
    sign_up_rozetka.clear_email()

    sign_up_rozetka.enter_email("$#2")
    sign_up_rozetka.assert_error_email("Введіть номер мобільного телефону")
    sign_up_rozetka.clear_email()
   
    sign_up_rozetka.enter_email("mail@")
    sign_up_rozetka.assert_error_email("Введіть номер мобільного телефону")


    #Перевірка поля "Придумайте пароль"
    sign_up_rozetka.enter_password("1A")
    sign_up_rozetka.assert_error_password("Не менше 6 символів")
    

    #Закриття сторінки "Реєстрація" на Rozetka.com.ua
    sign_up_rozetka.close()