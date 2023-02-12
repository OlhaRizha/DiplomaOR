import requests


class Github:

    def get_user(self,username):
        self.username=username
        URL='https://api.github.com/users/'+self.username
        r=requests.get(URL)
        body=r.json()

        return body

    
    def search_repo(self,name):
        r=requests.get('https://api.github.com/search/repositories',params={"q": name})
        body=r.json()

        return body

