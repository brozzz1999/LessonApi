import httpx
import allure

BASE_URL = 'https://reqres.in/api/users'

@allure.suite('Проверка запросов для работы с пользователями')
@allure.title('Метод удаляющий пользователя')
def test_user_delete():
    with allure.step('Выполняем DELETE запрос'):
        response = httpx.delete(BASE_URL + '/2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204

@allure.title('Создаем пользователя методом POST')
def test_create_user():

    with allure.step('Передаем имя, должность в теле запроса POST')
    body = {"name": "morpheus","job": "leader"}

    response = httpx.post(BASE_URL, json=body)
    print(response.json())
