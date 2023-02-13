import pytest
import requests

#Створення тесту з міткою http, що перевіряє  можливість відправки запиту GET та отримання відповіді
@pytest.mark.http
def test_first_request():
    r=requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}") 

#Ствоерння тесту з міткою http, що перевіряє можливість відправки запиту GET та чи тіло відповіді
# містить очікувані дані
@pytest.mark.http
def test_second_request():
    r=requests.get('https://api.github.com/users/defunkt')
    body=r.json()
    headers=r.headers
    assert r.status_code==200
    assert body['name']=='Chris Wanstrath'
    assert headers['Server']=='GitHub.com'

#Створення тесту з міткою http, що перевіряє що статус код відповіді на некоректний запит GET буде 404
@pytest.mark.http
def test_status_code_request():
    r=requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code==404