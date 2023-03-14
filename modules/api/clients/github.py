import requests


class Github:
    """
    Creating a class GitHub
    """

    def get_user(self, username):
        """
        Creating a method of the GitHub class object, which generates the URL address
         for the HTTP equest and returns the response in json format
         """

        self.username = username
        URL = 'https://api.github.com/users/'+self.username
        r = requests.get(URL)
        body = r.json()

        return body

    def search_repo(self, name):
        """
        Creates a method of the Github class object that returns the body of the response in JSON format
        by making an HTTP request with the 'q' parameter. This method will be used to search repositories on GitHub
        """

        r = requests.get(
            'https://api.github.com/search/repositories', params={"q": name})
        body = r.json()

        return body
