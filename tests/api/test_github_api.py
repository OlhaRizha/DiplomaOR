import pytest


@pytest.mark.api
def test_user_exists(github_api):
    """
    Test with the api tag, that checks the ability to search for a User's name on GitHub and 
    whether the response body matches the expected results (using the github_api fixture).
    """
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    """
    Test with the api tag, that checks the ability to search for a User's name on GitHub, 
    who does not exist and whether the response body matches the expected results 
    (using the github_api fixture).
    """
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    """
    Test with the api tag, that checks the ability to search for a repository by name on GitHub 
    and whether the response body matches the expected results (using the github_api fixture).
    """
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 32


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    """
    Test with the api tag, that checks the ability to search for a non-existent repository by name on GitHub 
    and whether the response body matches the expected results (using the github_api fixture).
    """
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
