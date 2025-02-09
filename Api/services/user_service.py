import allure
from Api.core.base_service import BaseService


class UserService(BaseService):
    def __init__(self):
        super().__init__("https://petstore.swagger.io/v2")

    @allure.step("Создание массива пользователей с данными : {users_data}")
    def create_users_with_array(self, users_data):
        return self.post("/user/createWithArray", data=users_data)