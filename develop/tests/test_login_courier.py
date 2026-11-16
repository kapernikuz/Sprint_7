import allure
from api.courier_api import CourierApi
from data import BASE_URL, ERROR_LOGIN_DATA, ERROR_LOGIN_NOT_FOUND

@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Успешный логин курьера")
    def test_login_success(self, courier):
        api = CourierApi(BASE_URL)
        response = api.login({"login": courier["login"], "password": courier["password"]})
        
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин с неверным паролем")
    def test_login_wrong_password(self, courier):
        api = CourierApi(BASE_URL)
        response = api.login({"login": courier["login"], "password": "wrong_password"})
        
        assert response.status_code == 404
        assert ERROR_LOGIN_NOT_FOUND in response.json()["message"]

    @allure.title("Логин без обязательного поля")
    def test_login_missing_field(self):
        api = CourierApi(BASE_URL)
        response = api.login({"password": "1234"})
        
        assert response.status_code == 400
        assert ERROR_LOGIN_DATA in response.json()["message"]