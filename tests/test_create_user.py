import pytest
import requests
import allure
from urls import Urls


class TestCreateUser:
    @allure.title('Проверка успешной регистрации пользователя')
    def test_create_user(self, create_user):
        create_user_data, response_data, status_code = create_user

        assert status_code == 200, 'Статус код должен быть 200 при успешной регистрации'
        assert 'accessToken' in response_data, 'В ответе должен присутствовать accessToken'
        assert 'refreshToken' in response_data, 'В ответе должен присутствовать refreshToken'


    @allure.title('Регистрация пользователя, который уже зарегистрирован')
    def test_register_exist_user(self, create_user):
        create_user_data, response_data, status_code = create_user
        response = requests.post(Urls.CREATE_USER, json=create_user_data)
        response_data = response.json()

        assert response.status_code == 403, "Статус код должен быть 403, если пользователь уже существует"
        assert response_data['success'] == False, "Поле 'success' должно быть False"
        assert response_data['message'] == 'User already exists', "Сообщение должно быть 'User already exists'"


    @allure.title('Регистрация пользователя без обязательных параметров (пароль, email, name)')
    @pytest.mark.parametrize("test_user_data", [
        {"email": "", "password": "qwerty", "name": "Test"},
        {"email": "test@example.com", "password": "", "name": "Test"},
        {"email": "test@example.com", "password": "qwerty", "name": ""}
    ])
    def test_create_user_without_required_field(self, test_user_data):
        response = requests.post(Urls.CREATE_USER, json=test_user_data)
        response_data = response.json()

        assert response.status_code == 403, "Статус код должен быть 403 при отсутствии обязательных полей"
        assert response_data['success'] == False, "Поле 'success' должно быть False"
        assert response_data['message'] == "Email, password and name are required fields", "Сообщение должно быть 'Email, password and name are required fields'"