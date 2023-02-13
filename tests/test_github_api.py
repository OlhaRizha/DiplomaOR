import pytest

#Cтворення тесту з міткою api, що перевіряє можливість пошуку імені Користувача на GitHub 
# та чи тіло відповіді відповідає очікуваним результатам
#(з використанням фікстури github_api)
@pytest.mark.api
def test_user_exists(github_api):
    user=github_api.get_user('defunkt')
    assert user['login']=='defunkt'

#Cтворення тесту з міткою api, що перевіряє можливість пошуку імені Користувача на GitHub 
# якого не існує та чи тіло відповіді відповідає очікуваним результатам
#(з використанням фікстури github_api)
@pytest.mark.api
def test_user_not_exists(github_api):
    r=github_api.get_user('butenkosergii')
    assert r['message']=='Not Found'

#Cтворення тесту з міткою api, що перевіряє можливість пошуку репозиторію за назвою на GitHub 
# та чи тіло відповіді відповідає очікуваним результатам
#(з використанням фікстури github_api)
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r=github_api.search_repo('become-qa-auto')
    assert r['total_count']==30

#Cтворення тесту з міткою api, що перевіряє можливість пошуку неіснуючого репозиторію за назвою на GitHub 
# та чи тіло відповіді відповідає очікуваним результатам
#(з використанням фікстури github_api)    
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r=github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count']==0
    