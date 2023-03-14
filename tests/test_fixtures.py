import pytest


@pytest.mark.check
def test_change_name(user):
    """
    Test that changes the user's name to "Olha" using the "user" fixture.
    """
    assert user.name == 'Olha'


@pytest.mark.check
def test_change_second_name(user):
    """
    Test that changes the user's second name to "Ryzha" using the "user" fixture.
    """
    assert user.second_name == 'Ryzha'
