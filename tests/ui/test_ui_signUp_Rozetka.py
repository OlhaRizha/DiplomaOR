from modules.ui.page_objects import sign_up_rozetka
from modules.ui.page_objects.sign_up_rozetka import SignUpRozetka
import pytest


@pytest.mark.rozetka
def test_check_signup_name():
    """
    Test that creates an object of the SignUpRozetka class, checks the ability to open the registration page of the
    Rozetka.com.ua website, and verifies the ability to enter incorrect data for registration and checks the error message
    displayed in response to this action
    """
    sign_up_rozetka = SignUpRozetka()

    sign_up_rozetka.go_to()

    sign_up_rozetka.open_registration_window()

    """
    This test is checks the "Name" field
    """
    sign_up_rozetka.enter_name("12345")
    sign_up_rozetka.assert_error_name()
    sign_up_rozetka.clear_name()

    sign_up_rozetka.enter_name("%&*")
    sign_up_rozetka.assert_error_name()
    sign_up_rozetka.clear_name()

    sign_up_rozetka.enter_name("username")
    sign_up_rozetka.assert_error_name()

    sign_up_rozetka.close()


# Перевірка поля "Прізвище"
@pytest.mark.rozetka
def test_check_signup_second_name():
    sign_up_rozetka = SignUpRozetka()

    sign_up_rozetka.go_to()

    sign_up_rozetka.open_registration_window()

    """
    This test is checks the "Second Name" field
    """

    sign_up_rozetka.enter_second_name("6578")
    sign_up_rozetka.assert_error_second_name()
    sign_up_rozetka.clear_second_name()

    sign_up_rozetka.enter_second_name("#$@")
    sign_up_rozetka.assert_error_second_name()
    sign_up_rozetka.clear_second_name()

    sign_up_rozetka.enter_second_name("secondname")
    sign_up_rozetka.assert_error_second_name()

    sign_up_rozetka.close()


# Перевірка поля "Номер телефону"
@pytest.mark.rozetka
def test_check_signup_phone_number():
    sign_up_rozetka = SignUpRozetka()

    sign_up_rozetka.go_to()

    sign_up_rozetka.open_registration_window()
    """
    This test is checks the "Phone Number" field
    """

    sign_up_rozetka.enter_phone_number("1111111111")
    sign_up_rozetka.assert_error_phone_number()

    sign_up_rozetka.close()


# Перевірка поля "Ел.пошта"
@pytest.mark.rozetka
def test_check_signup_email():
    sign_up_rozetka = SignUpRozetka()

    sign_up_rozetka.go_to()

    sign_up_rozetka.open_registration_window()
    """
    This test is checks the "Email" field
    """

    sign_up_rozetka.enter_email("123")
    sign_up_rozetka.assert_error_email()
    sign_up_rozetka.clear_email()

    sign_up_rozetka.enter_email("$#2")
    sign_up_rozetka.assert_error_email()
    sign_up_rozetka.clear_email()

    sign_up_rozetka.enter_email("mail@")
    sign_up_rozetka.assert_error_email()

    sign_up_rozetka.close()


# Перевірка поля "Придумайте пароль"
@pytest.mark.rozetka
def test_check_signup_password():
    sign_up_rozetka = SignUpRozetka()

    sign_up_rozetka.go_to()

    sign_up_rozetka.open_registration_window()
    """
    This test is checks the "Think a password" field
    """

    sign_up_rozetka.enter_password("1A")
    sign_up_rozetka.assert_error_password()

    # Закриття сторінки "Реєстрація" на Rozetka.com.ua
    sign_up_rozetka.close()
