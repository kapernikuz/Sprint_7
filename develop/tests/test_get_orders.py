import allure
from api.order_api import OrderApi
from data import BASE_URL

@allure.feature("Получение списка заказов")
class TestGetOrders:
    @allure.title("Успешное получение списка заказов")
    def test_get_orders_list(self):
        api = OrderApi(BASE_URL)
        response = api.get_orders()
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)