import pytest
from api.courier_api import CourierApi
from data import BASE_URL
from helpers import generate_random_string


@pytest.fixture
def courier():
    """Создает уникального курьера перед тестом и удаляет его после."""
    api = CourierApi(BASE_URL)
    login = generate_random_string()
    payload = {"login": login, "password": "1234", "firstName": "Test"}
    
    api.create(payload)
    yield payload
    
    # Удаляем курьера после теста
    login_response = api.login({"login": login, "password": "1234"})
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        api.delete(courier_id)