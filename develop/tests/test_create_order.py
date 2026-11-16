import allure
import pytest
from api.order_api import OrderApi
from data import BASE_URL

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_colors(self, color):
        api = OrderApi(BASE_URL)
        payload = {
            "firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.",
            "metroStation": 4, "phone": "+7 800 355 35 35", "rentTime": 5,
            "deliveryDate": "2026-11-20", "comment": "Saske, come back to Konoha", "color": color
        }
        response = api.create(payload)
        
        assert response.status_code == 201
        assert "track" in response.json()