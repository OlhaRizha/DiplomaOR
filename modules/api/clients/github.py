import requests

#Створення класу GitHub
class Github:

#Створення методу об'єкту класу GitHub, що формує URL адресу для HTTP запиту та повертає відповідь у форматі json
    def get_user(self,username):
        self.username=username
        URL='https://api.github.com/users/'+self.username
        r=requests.get(URL)
        body=r.json()

        return body

#Створення методу об'єкту класу GitHub, який за допомогою НТТР запиту з параметром q повертає тіло відповіді у форматі json
#На основі цього методу буде створений тест для пошуку репозиторію на GitHub 
    def search_repo(self,name):
        r=requests.get('https://api.github.com/search/repositories',params={"q": name})
        body=r.json()

        return body


