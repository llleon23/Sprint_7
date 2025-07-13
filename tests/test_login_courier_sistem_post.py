import allure
import pytest
import requests
import curl
from data import *


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера в системе")
    def test_login_courier_success(self, crete_courier_authorization):
        response = requests.post(curl.LOGIN_COURIER_URL, json=crete_courier_authorization[1])
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Авторизация курьера без обязательных полей логин и пароль")
    @pytest.mark.parametrize('not_field', DataEnterNoValid.enter_data)
    def test_not_login_or_password(self, not_field):
        response = requests.post(curl.LOGIN_COURIER_URL, not_field)
        assert response.status_code == 400 and response.json() == DataResponse.RESP_LOGIN_PASSWORD_NO_DATA

    @allure.title("Авторизация курьера несуществующими логином и паролем")
    def test_non_existent_login_password(self):
        non_existent = {'login': helper.fake_login(), 'password': helper.fake_password()}
        response = requests.post(curl.LOGIN_COURIER_URL, non_existent)
        assert response.status_code == 404 and response.json() == DataResponse.RESP_LOGIN_PASSWORD_NO_VALID
