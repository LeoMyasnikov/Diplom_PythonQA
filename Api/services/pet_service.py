import allure
from Api.core.base_service import BaseService


class PetService(BaseService):
    def __init__(self):
        super().__init__("https://petstore.swagger.io/v2")

    @allure.step("Поиск питомца по ID: {pet_id}")
    def find_pet_by_id(self, pet_id):
        return self.get(f"/pet/{pet_id}")

    @allure.step("Добавление нового питомца")
    def add_new_pet(self, pet_data):
        return self.post("/pet", data=pet_data)