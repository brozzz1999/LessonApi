import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA, SINGLE_USER_SUPPORT
import allure

BASE_URL = 'https://reqres.in/api/users'
EMAIL_ENDS = '@reqres.in'


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод проверяющий список пользователей')
def test_list_users():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + '?page=2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    users_data = response.json()['data']
    for item in users_data:
        with allure.step('Сверяем ответ с контрактом'):
            validate(item, USER_DATA_SCHEMA)

        with allure.step(f'Проверяем, что email оканчивается на {EMAIL_ENDS}'):
            assert item['email'].endswith(EMAIL_ENDS)


@allure.title('Метод проверяющий одного пользователя')
def test_single_usser():
    with allure.step('Выполняем GET запрос'):
        response_user = httpx.get(BASE_URL + '/2')

    with allure.step('Проверяем ккод ответа'):
        assert response_user.status_code == 200

    user_data = response_user.json()['data']
    with allure.step('Сверяем ответ с контрактом'):
        validate(user_data, USER_DATA_SCHEMA)

    user_support = response_user.json()['support']
    with allure.step('Сверяем ответ с контрактом support'):
        validate(user_support, SINGLE_USER_SUPPORT)
