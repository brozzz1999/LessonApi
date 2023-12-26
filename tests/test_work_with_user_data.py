import httpx
import allure
import pytest
import json

BASE_URL = 'https://reqres.in/api/users'
BASE_URL_REGISTER = 'https://reqres.in/api/register'


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

