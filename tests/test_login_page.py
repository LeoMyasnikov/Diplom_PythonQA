import time
import allure
from pages.login_page import LoginPage
from pages.edit_page import EditPage
from pages.personal_page import PersonalPage


@allure.feature('LoginPage')
class TestLoginPage():
    @allure.story("Проверка открытия страницы логина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.assert_page_is_opened()

    @allure.story("Проверка авторизации с корректными кредами")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials()

        personal_page = PersonalPage(driver)
        personal_page.assert_page_is_opened()

    @allure.story("Проверка, что учетная запись заблокируется после введения несколько раз некорректного пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_account_lockout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_incorrect_password()

    @allure.story("Проверка, что при вводе дефолтного пароля, пользователя должно перекинуть на страницу смены пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_password_after_default(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_default_credentials()

        edit_page = EditPage(driver)
        edit_page.assert_edit_page_is_opened()

    @allure.story("Проверка смена языка комплекса")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_language(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.change_language()

    @allure.story("Проверка, что пользователь с некорректным логином не сможет авторизоваться")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_incorrect_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_incorrect_login()
        login_page.assert_incorrect_login()

    @allure.story("Проверка актуальности справки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_help(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.open_help()
        login_page.assert_open_help()

    @allure.story("Проверка корректности копирайтов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_copywrite(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.copyrighting_check()








