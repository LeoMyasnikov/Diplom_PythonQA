import allure
from Api.services.user_service import UserService
from Api.data.user_data import user_data
from Api.core.assertions import Assertions


@allure.suite("Тесты для сервиса User")
class TestUser:
    def test_create_users_with_array(self):
        service = UserService()
        response = service.create_users_with_array(user_data)
        Assertions.assert_status_code(response, 200)