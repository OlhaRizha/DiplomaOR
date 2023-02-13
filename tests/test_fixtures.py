import pytest

#Створення тесту з маркуванням check, що змінює ім'я користувача на 'Olha'
#(використовуючи фікстуру user)
@pytest.mark.check
def test_change_name(user):
    assert user.name=='Olha'

#Створення тесту з маркуванням check, що змінює фамілію користувача на 'Ryzha'
#(використовуючи фікстуру user)
@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name=='Ryzha'

