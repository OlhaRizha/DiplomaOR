import pytest


@pytest.mark.change
def test_remove_name(user):
    """
    Test to check if the name of the user created in the User class can be removed
    using the fixture 'user'.
    """
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    """
    Test to check if the user created in the User class has the name 'Olha'
    using the fixture 'user'.
    """
    assert user.name == 'Olha'


@pytest.mark.check
def test_second_name(user):
    """
    Test to check if the user created in the User class has the last name 'Ryzha'
    using the fixture 'user'.
    """
    assert user.second_name == 'Ryzha'
