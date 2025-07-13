import allure
import pytest
import requests
import curl
from data import *


class TestCreateCourier:
    @allure.title("Успешное создании курьера")
    def test_create_courier_success(self, crete_courier_data):
        courier_data = crete_courier_data[0]
        response = requests.post(curl.CREATE_COURIER_URL, json=courier_data)
        assert response.status_code == 201 and (response.json() == DataResponse.RESP_CREATE_COURIER_OK)

    @allure.title("Создание курьера без обязательных полей логин и пароль")
    @pytest.mark.parametrize('not_field', DataRegistration.registration_data)
    def test_create_courier_missing_field(self, not_field):
        response = requests.post(curl.CREATE_COURIER_URL, not_field)
        assert response.status_code == 400 and (response.json() == DataResponse.RESP_CREATE_COURIER_NO_LOGIN)

    @allure.title("Создании пользователя с логином, который уже есть")
    def test_create_duplicate_courier(self, crete_courier_data):
        courier_data = crete_courier_data[0]
        requests.post(curl.CREATE_COURIER_URL, json=courier_data)
        response = requests.post(curl.CREATE_COURIER_URL, json=courier_data)
        assert response.status_code == 409 and (response.json() == DataResponse.RESP_CREATE_COURIER_REPEAT)
