import pytest
import allure
import requests
import helpers.helpers
from data.data import *


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

    @allure.title('Проверка авторизации с несуществующими учетными данными')
    def test_login_user_not_exist(self, create_and_delete_user):
        payload = {"email": helpers.helpers.email, "password": helpers.helpers.password}
        response = requests.post(Links.login_url, data=payload)
        assert response.status_code == 401 and response.json()['message'] == "email or password are incorrect"


class TestUpdateUser:
    @allure.title('Изменение имени авторизованного пользователя')
    def test_update_user_name_of_signed_in_user(self, create_and_delete_user):
        new_name = {"name": helpers.helpers.name}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Links.user_url, headers=token, data=new_name)
        assert response.status_code == 200 and response.json()['user']['name'] in str(new_name)

    @allure.title('Изменение почты авторизованного пользователя')
    def test_update_user_email_of_signed_in_user(self, create_and_delete_user):
        new_email = {"email": helpers.helpers.email}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Links.user_url, headers=token, data=new_email)
        assert response.status_code == 200 and response.json()['user']['email'] in str(new_email)

    @allure.title('Попытка изменения почты авторизованного пользователя на уже существующую почту')
    def test_update_user_email_of_signed_in_user(self, create_and_delete_user):
        new_email = {"email": create_and_delete_user[2]['email']}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Links.user_url, headers=token, data=new_email)
        assert response.status_code == 403 and response.json()['message'] == "User with such email already exists"

    @allure.title('Изменение пароля авторизованного пользователя')
    def test_update_user_password_of_signed_in_user(self, create_and_delete_user):
        new_password = {"password": "uuuu"}
        token = {'Authorization': create_and_delete_user[3]}
        requests.patch(Links.user_url, headers=token, data=new_password)
        payload = {"email": create_and_delete_user[2]['email'], "password": "uuuu"}
        response = requests.post(Links.login_url, data=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize('payload', [{'name': helpers.helpers.name},{'email': helpers.helpers.email},
        {'password': helpers.helpers.password}])
    def test_update_user_data_without_authorization(self, payload):
        response = requests.patch(Links.user_url, data=payload)
        assert response.status_code == 401 and response.json()['message'] == "You should be authorised"
