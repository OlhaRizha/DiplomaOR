import pytest

#Створення тесту з міткою change, що перевіряє можливість 
# видалення імені Користувача, створеного в класі User
#(використовуючи фікстуру user)
@pytest.mark.change
def test_remove_name(user):
    user.name=''
    assert user.name==''

#Створення тесту з міткою check, що перевіряє чи було присвоєно Користувачу ім'я 'Olha'
#(використовуючи фікстуру user)
@pytest.mark.check
def test_name(user):
    assert user.name=='Olha'

#Створення тесту з міткою check, що перевіряє чи було присвоєно Користувачу прізвище 'Ryzha'
#(використовуючи фікстуру user)
@pytest.mark.check
def test_second_name(user):
    assert user.second_name=='Ryzha'



