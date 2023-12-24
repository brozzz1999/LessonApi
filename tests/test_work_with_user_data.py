import httpx
import allure
import pytest
import json

from jsonschema import validate
from core.contracts import SUCCESSFUL_LOGIN_SHEMA

BASE_URL = 'https://reqres.in/api/users'
BASE_URL_REGISTER = 'https://reqres.in/api/register'
LOGIN_URL = 'https://reqres.in/api/login'


@allure.suite('Проверка запросов для работы с пользователями')
@allure.title('Метод удаляющий пользователя')
def test_user_delete():
    with allure.step('Выполняем DELETE запрос'):
        response = httpx.delete(BASE_URL + '/2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204


json_file = open('./users_credentials.json')
users_credentials = json.load(json_file)


@allure.title('Создаем пользователей методом POST из файла json')
@pytest.mark.parametrize("user_credentials", users_credentials)
def test_create_user(user_credentials):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Передаем имя, должность в теле запроса POST'):
        response = httpx.post(BASE_URL, json=user_credentials, headers=headers)
    print(response.json())


json_file_register = open('./users_register.json')
users_register = json.load(json_file_register)


@allure.title('Регистрируем пользователей методом POST из файла json')
@pytest.mark.parametrize("user_register", users_register)
def test_register_successful(user_register):
    headers = {'Content-Type': 'application/json'}
    response = httpx.post(BASE_URL_REGISTER, json=user_register, headers=headers)

    print(response.json())

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

@allure.title('Успешная проверка авторизации пользователя')
def test_successful_login():
    users_login_password = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post(LOGIN_URL, json=users_login_password, headers=headers)
    assert response.status_code == 200
    validate(response.json(), SUCCESSFUL_LOGIN_SHEMA)


@allure.title('НЕ успешная проверка авторизации пользователя')
def test_unsuccessful_login():
    users_login_password = {
        "email": "eve.holt@reqres.in",
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post(LOGIN_URL, json=users_login_password, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400

    with allure.step('Проверяем текст ответа'):
        assert response.json()['error'] == 'Missing password'

@allure.title('НЕ верный логин')
def test_wrong_login():
    users_login_password = {
        "email": "eve.holt@reqre.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post(LOGIN_URL, json=users_login_password, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400

    with allure.step('Проверяем текст ошибки "Пользователь не найден'):
        assert response.json()['error'] == 'user not found'
