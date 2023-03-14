import pytest
from modules.api.clients.github import Github


class User:
    """
    Class for creating test users and testing their creation, 
    name change, existence, and deletion
    """

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Olha'
        self.second_name = 'Ryzha'

    def remote(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    """
    Method for creating a test user with a name 
    and a second name
    """
    user = User()
    user.create()

    yield user

    user.remote()


@pytest.fixture
def github_api():
    """
    Method for removing the test user's name and second name
    """
    api = Github()
    yield api
