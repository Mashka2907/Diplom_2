import pytest
import requests
import allure
from urls import Urls
from data import Data


class TestUpdateUser:
    @allure.title('Изменение данных с авторизованным пользователем - поле email')
    def test_update_user_email_with_auth(self, create_user):
        create_user_data, response_data, status_code = create_user
        access_token = response_data.get('accessToken')
        response = requests.patch(Urls.USER_UPDATE, headers={"Authorization": access_token}, json=Data.UPDATE_EMAIL)
        response_data = response.json()

        assert response.status_code == 200, "Статус код должен быть 200"
        assert response_data['success'] == True, "Поле 'success' должно быть True"
        assert response_data['user']['email'] == Data.UPDATE_EMAIL['email']


    @allure.title('Изменение данных с авторизованным пользователем - поле name')
    def test_update_user_name_with_auth(self, create_user):
        create_user_data, response_data, status_code = create_user
        access_token = response_data.get('accessToken')
        response = requests.patch(Urls.USER_UPDATE, headers={"Authorization": access_token}, json=Data.UPDATE_NAME)
        response_data = response.json()

        assert response.status_code == 200, "Статус код должен быть 200"
        assert response_data['success'] == True, "Поле 'success' должно быть True"
        assert response_data['user']['name'] == Data.UPDATE_NAME['name']


    @allure.title('Изменение данных не авторизованным пользователем - поле email')
    def test_update_user_email_without_auth(self):
        response = requests.patch(Urls.USER_UPDATE, json=Data.UPDATE_EMAIL)
        response_data = response.json()

        assert response.status_code == 401, "Статус код должен быть 401"
        assert response_data['success'] == False, "Поле 'success' должно быть False"
        assert response_data['message'] == 'You should be authorised', "Сообщение должно быть 'You should be authorised'"


    @allure.title('Изменение данных не авторизованным пользователем - поле name')
    def test_update_user_name_without_auth(self):
        response = requests.patch(Urls.USER_UPDATE, json=Data.UPDATE_NAME)
        response_data = response.json()

        assert response.status_code == 401, "Статус код должен быть 401"
        assert response_data['success'] == False, "Поле 'success' должно быть False"
        assert response_data['message'] == 'You should be authorised', "Сообщение должно быть 'You should be authorised'"
