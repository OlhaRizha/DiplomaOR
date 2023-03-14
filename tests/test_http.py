import pytest
import requests


@pytest.mark.http
def test_first_request():
    """
    Test with http marker that checks the ability to send a GET request and receive a response.
    """
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    """
    Test with http marker that checks the ability to send a GET request and whether the body of the response 
    contains the expected data.
    """
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers
    assert r.status_code == 200
    assert body['name'] == 'Chris Wanstrath'
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    """
    Test with http marker that checks that the status code of the response to an incorrect GET request is 404.
    """
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404
