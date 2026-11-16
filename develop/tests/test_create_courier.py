import allure
from api.courier_api import CourierApi
from data import BASE_URL, ERROR_CREATE_COURIER, ERROR_LOGIN_TAKEN
from helpers import generate_random_string


@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        api = CourierApi(BASE_URL)
        login = generate_random_string()
        payload = {"login": login, "password": "1234", "firstName": "Test"}
        
        response = api.create(payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        # Удаляем созданного курьера (чтобы не оставлять мусор)
        login_response = api.login({"login": login, "password": "1234"})
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            api.delete(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        api = CourierApi(BASE_URL)
        login = generate_random_string()
        payload = {"login": login, "password": "1234", "firstName": "Test"}
        
        api.create(payload)
        response = api.create(payload)
        
        assert response.status_code == 409
        assert ERROR_LOGIN_TAKEN in response.json()["message"]
        
        # Удаляем созданного курьера
        login_response = api.login({"login": login, "password": "1234"})
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            api.delete(courier_id)

    @allure.title("Создание курьера без обязательного поля")
    def test_create_courier_missing_field(self):
        api = CourierApi(BASE_URL)
        payload = {"password": "1234", "firstName": "Test"}  # Нет логина
        response = api.create(payload)
        
        assert response.status_code == 400
        assert ERROR_CREATE_COURIER in response.json()["message"]