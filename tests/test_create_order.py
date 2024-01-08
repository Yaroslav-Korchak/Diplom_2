import allure
import requests
from data.data import *


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    def test_create_order_successful_with_authorisation(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.post(Links.ORDER_URL, headers=token, data=TestOrder.successful_order)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_successful_without_authorisation(self, create_and_delete_user):
        response = requests.post(Links.ORDER_URL, data=TestOrder.successful_order)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_successful_without_ingredients(self, create_and_delete_user):
        response = requests.post(Links.ORDER_URL)
        assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Проверка создания заказа c неправильным хешем ингредиентов')
    def test_create_order_successful_with_wrong_hash_of_ingredient(self, create_and_delete_user):
        response = requests.post(Links.ORDER_URL, data=TestOrder.bad_order)
        assert response.status_code == 500
