import pytest

from library.api.swapi_clients.people_client import PeopleSwapi


@pytest.fixture
def people_api():
    return PeopleSwapi()


def test_get_all_people(people_api):
    response = people_api.get_all()
    assert response.status_code == 200
    assert response.json()['count'] == 82