import pytest
import requests
from data.data import Links
import random
import string


@pytest.fixture
def create_and_delete_user():
    def random_generator(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = random_generator(10)
    email = random_generator(10)+'@yandex.ru'
    password = random_generator(10)

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    login_data = payload.copy()
    login_data.pop("name")
    response = requests.post(Links.register_url, data=payload)
    access_token = response.json()["accessToken"]
    yield response, payload, login_data, access_token
    requests.delete(Links.user_url, headers={'Authorization': access_token})


