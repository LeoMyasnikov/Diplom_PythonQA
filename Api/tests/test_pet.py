import allure
from Api.services.pet_service import PetService
from Api.data.pet_data import pet_data
from Api.core.assertions import Assertions


@allure.suite("Тесты для сервиса Pet")
class TestPet:
    def test_find_pet_by_id(self):
        service = PetService()
        response = service.find_pet_by_id(2)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_response_value(response, "name", "2 dinosaur")

    def test_add_new_pet(self):
        service = PetService()
        response = service.add_new_pet(pet_data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_response_key_exists(response, "id")
        Assertions.assert_response_value(response, "name", pet_data["name"])
