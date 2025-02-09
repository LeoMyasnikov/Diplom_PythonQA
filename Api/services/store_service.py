import allure
from Api.core.base_service import BaseService


class StoreService(BaseService):
    def __init__(self):
        super().__init__("https://petstore.swagger.io/v2")

    @allure.step("Размещение заказа на питомца")
    def place_order_for_pet(self, order_data):
        return self.post("/store/order", data=order_data)

    @allure.step("Удаление заказа по ID")
    def delete_order_by_id(self, order_id):
        return self.delete(f"/store/order/{order_id}")