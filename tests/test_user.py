import pytest
import allure
import requests

import helpers.helpers
from data.data import *
from helpers.helpers import *


class TestCreateUser:
    @allure.title('Проверка успешной регистрации пользователя')
    def test_create_new_user_success(self, create_and_delete_user):
        status = create_and_delete_user[0]
        assert status.status_code == 200 and "accessToken" in status.json()

    @allure.title('Проверка создания пользователя с уже существующими данными')
    def test_create_already_existing_user(self, create_and_delete_user):
        response = requests.post(Links.register_url, data=create_and_delete_user[1])
        assert response.status_code == 403 and response.json()['message'] == "User already exists"

    @allure.title('Проверка создания пользователя без обязательных полей')
    @pytest.mark.parametrize('payload', (
    UserWithoutRequiredFields.no_name, UserWithoutRequiredFields.empty_name, UserWithoutRequiredFields.no_password,
    UserWithoutRequiredFields.empty_password, UserWithoutRequiredFields.no_email, UserWithoutRequiredFields.empty_email))
    def test_create_user_without_required_fields_fail(self, payload):
        response = requests.post(Links.register_url, data=payload)

        assert response.status_code == 403 and response.json()['message'] == "Email, password and name are required fields"


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    def test_user_login_success(self, create_and_delete_user):
        response = requests.post(Links.login_url, data=create_and_delete_user[2])
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка авторизации с несуществующими кредами')
    def test_login_user_not_exist(self, create_and_delete_user):
        payload = {"email": helpers.helpers.email, "password": helpers.helpers.password}
        response = requests.post(Links.login_url, data=payload)
        assert response.status_code == 401 and response.json()['message'] == "email or password are incorrect"
