from api.base_api import BaseApi
from data import COURIER, COURIER_LOGIN

class CourierApi(BaseApi):
    def create(self, payload):
        return self.post(COURIER, data=payload)

    def login(self, payload):
        return self.post(COURIER_LOGIN, data=payload)

    def delete(self, courier_id):
        return super().delete(f"{COURIER}/{courier_id}")