from sancaqa.api.api_client import APIClient


class PeopleSwapi(APIClient):
    def __init__(self):
        super(PeopleSwapi, self).__init__()
        self.url = "https://swapi.dev/api/people"

    def get_all(self):
        return self.get(self.url)
