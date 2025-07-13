import pytest
import curl
import helper
import requests

@pytest.fixture
def crete_courier_authorization():
    login = helper.fake_login()
    password =  helper.fake_password()
    first_name = helper.fake_firstname()
    create_courier_data = {'login': login, 'password': password,'firstName': first_name}
    login_courier_data =  {'login': login, 'password': password}
    requests.post(curl.CREATE_COURIER_URL, json=create_courier_data)
    login_courier = requests.post(curl.LOGIN_COURIER_URL, json=login_courier_data)
    yield [create_courier_data, login_courier_data, login, password]
    requests.delete(f'{curl.DELETE_COURIER_URL}{login_courier.json()["id"]}')


@pytest.fixture
def crete_courier_data():
    login = helper.fake_login()
    password =  helper.fake_password()
    first_name = helper.fake_firstname()
    create_courier_data = {'login': login, 'password': password,'firstName': first_name}
    login_courier_data =  {'login': login, 'password': password}
    yield [create_courier_data, login_courier_data]
    login_courier = requests.post(curl.LOGIN_COURIER_URL, json=login_courier_data)
    requests.delete(f'{curl.DELETE_COURIER_URL}{login_courier.json()["id"]}')
