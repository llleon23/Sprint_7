import allure
import pytest
import requests
import curl
from data import *


class TestCreatingOrder:
    @allure.title("Создание заказа с выбором цветов")
    @pytest.mark.parametrize('color_selection', DataListOrders.color_scooter)
    def test_creating_order_scooter_color(self, color_selection):
        list_order = DataListOrders.list_order
        list_order['color'] = color_selection
        response = requests.post(curl.CREATE_ORDER_URL, json=list_order)
        assert response.status_code == 201 and DataResponseData.RESPONSE_ID_ORDER in response.json()
