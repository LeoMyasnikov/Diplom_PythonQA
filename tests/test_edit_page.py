import allure
from pages.edit_page import EditPage
from pages.login_page import LoginPage


@allure.feature('EditPage')
class TestEditPage():
    @allure.story("Открытие страницы редактирования пользовательских данных")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_edit_page(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.assert_edit_page_is_opened()

    @allure.story("Проверка на слишком простой пароль")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_simple_password_verification(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.enter_credentials_with_simple_password()
        edit_page.assert_error_simple_password()

    @allure.story("Проверка на изменение кредов без логина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_without_login_verification(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.enter_credentials_without_login()
        edit_page.assert_error_without_login()

    @allure.story("Проверка на изменение кредов без пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_without_password_verification(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.enter_credentials_without_new_password()
        edit_page.assert_error_without_new_password()

    @allure.story("Проверка, что после отмены изменений происходит возвращение на страницу логина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_сhange_reversal(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.change_reversal()
        login_page = LoginPage(driver)
        login_page.assert_page_is_opened()







