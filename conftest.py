import pytest
from modules.api.clients.github import Github

#Створення класу User, на основі якого будуть створені тести 
# (що перевіряють можливість створення користувача, зміни імені користувача, його наявність 
# та можливість його видалення)
class User:

    def __init__(self):  
        self.name=None
        self.second_name=None

    def create(self):
        self.name='Olha'
        self.second_name='Ryzha'

    def remote(self):
        self.name=''
        self.second_name=''

#Створення фікстури на основі класу User
@pytest.fixture
def user():
    user=User()
    user.create()

    yield user

    user.remote()

#Створення фікстури на основі класу GitHub
@pytest.fixture
def github_api():
    api=Github()
    yield api
    