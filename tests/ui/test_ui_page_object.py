from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_data_for_sign_in_page():
    """
    Test that creates an object of the SignInPage class, 
    open the GitHub Login web page and enter user data, check data for login, 
    checks if the name of the given page is correct and closes the page"""
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("example@mail.com", "wrongpassword")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()
