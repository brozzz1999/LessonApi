import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SHEMA, SINGLE_RESOURCE_SUPPORT_SHEMA
import allure

BASE_URL = 'https://reqres.in/api/unknown'


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод проверяющий список ресурсов')
def test_list_resouce():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    resource_data = response.json()['data']
    for item in resource_data:
        with allure.step('Сверяем ответ с контрактом'):
            validate(item, RESOURCE_DATA_SHEMA)


@allure.title('Метод проверяющий один ресурс')
def single_resource():
    with allure.step('Выполняем GET запрос'):
        single_resource_response = httpx.get(BASE_URL + '/2')

    with allure.step('Проверяем код ответа'):
        assert single_resource_response.status_code == 200

    single_resource_data = single_resource_response.json()['data']

    with allure.step('Сверяем ответ с контрактом'):
        validate(single_resource_data, RESOURCE_DATA_SHEMA)

    resource_support = single_resource_response.json()['support']

    with allure.step('Сверяем ответ с контрактом support'):
        validate(resource_support, SINGLE_RESOURCE_SUPPORT_SHEMA)


@allure.title('Метод проверяющий что ресурс не существует')
def single_resource_not_found():
    with allure.step('Выполняем GET запрос'):
        single_resource_not_found_response = httpx.get(BASE_URL + '/23')

    with allure.step('Проверяем код ответа'):
        assert single_resource_not_found_response.status_code == 400
