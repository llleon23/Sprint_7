import allure
import requests
import curl
from data import DataResponseData


class TestGettingListOrder:
    @allure.title("Успешное получение списка заказов")
    def test_getting_list_success(self):
        response = requests.get(curl.GETTING_ORDERS_URL)
        assert response.status_code == 200 and DataResponseData.RESPONSE_DATA_SUCCESS in response.json()
