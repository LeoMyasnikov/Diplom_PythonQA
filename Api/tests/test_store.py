import allure
from Api.tests.conftest import create_order
from Api.services.store_service import StoreService
from Api.data.store_data import order_data
from Api.core.assertions import Assertions


@allure.suite("Тестирование заказов")
class TestStore:

    def test_place_order_for_pet(self):
        service = StoreService()
        response = service.place_order_for_pet(order_data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_response_key_exists(response, "id")
        Assertions.assert_response_value(response, "status", "placed")

    def test_delete_order_by_id(self, create_order):
        service = StoreService()
        response = service.delete_order_by_id(create_order)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_response_value(response, "message", str(create_order))
