from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

#Створення теста з міткою ui, що створює об'єкт класу SignInPage,
# перевіряє можливість відкрити веб сторінку Sign In сайту GitHub та введення даних користувача, 
# необхідних для входу, перевіряє чи назва даної сторінки так як очікується та закриває цю сторінку
@pytest.mark.ui
def test_check_incorrect_data_for_sign_in_page():
    sign_in_page=SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("example@mail.com","wrongpassword")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()