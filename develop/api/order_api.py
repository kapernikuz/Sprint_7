from api.base_api import BaseApi
from data import ORDERS

class OrderApi(BaseApi):
    def create(self, payload):
        return self.post(ORDERS, json=payload)

    def get_orders(self, params=None):
        return self.get(ORDERS, params=params)