import requests
import allure

class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("POST запрос на {endpoint}")
    def post(self, endpoint, data=None, json=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json)

    @allure.step("GET запрос на {endpoint}")
    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    @allure.step("DELETE запрос на {endpoint}")
    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}")