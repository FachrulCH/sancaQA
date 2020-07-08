from library.api import helper
from library.api.helper import API


def test_get_people():
    API().get("https://swapi.dev/api/people/1").assert_status_code(500)