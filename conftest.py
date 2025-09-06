import pytest
import requests
from faker import Faker
from urls import Urls

fake = Faker()

@pytest.fixture
def create_user():
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    response = requests.post(Urls.CREATE_USER, json=user_data)
    response_data = response.json()

    yield user_data, response_data, response.status_code

    access_token = response_data.get('accessToken')
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})