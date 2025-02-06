import pytest
from Api.core.assertions import Assertions
from Api.services.store_service import StoreService
from Api.data.store_data import order_data


@pytest.fixture
def create_order():
    """Фикстура для создания заказа перед тестом"""
    service = StoreService()
    response = service.place_order_for_pet(order_data)
    Assertions.assert_status_code(response, 200)
    return response.json().get("id")