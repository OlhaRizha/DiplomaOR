from modules.ui.page_objects.sign_up_page import SignUpPage
import pytest


@pytest.mark.signup
def test_check_incorrect_data_for_sign_up_page():
    """
    Test that creates an object of the SignUpPage class, 
    tests for the ability to open the GitHub Sign Up web page, 
    tests for the ability to enter an existing user's email to complete the signup, 
    and checks for an error in response to this action
    """
    sign_up_page = SignUpPage()

    sign_up_page.go_to()

    sign_up_page.enter_email("olharizha@gmail.com")

    sign_up_page.check_error("Email is invalid or already taken")

    sign_up_page.close()
