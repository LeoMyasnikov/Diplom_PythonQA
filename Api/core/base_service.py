import requests
import allure


class BaseService:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Выполнение GET-запроса к {endpoint}")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        allure.attach(
            body=str(response.json()),
            name="Тело ответа",
            attachment_type=allure.attachment_type.JSON
        )
        return response

    @allure.step("Выполнение POST-запроса к {endpoint} с данными: {data}")
    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        allure.attach(
            body=str(response.json()),
            name="Тело ответа",
            attachment_type=allure.attachment_type.JSON
        )
        return response

    @allure.step("Выполнение DELETE-запроса к {endpoint}")
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        allure.attach(
            body=str(response.text),
            name="Тело ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        return response