import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from core.base import Base
from data.cridentials import DOMAIN
from pages.login_page import loginPage


class EditPage(Base):

    edit_page = (By.XPATH, "//div[text()='Редактировать данные']")
    login_input = (By.CSS_SELECTOR, "[data-bind*='textInput: Login']")
    password_input = (By.CSS_SELECTOR, "[data-bind*='textInput: OldPassword']")
    password_new_input = (By.CSS_SELECTOR, "[data-bind*='textInput: Password']")
    repeat_password_new_input = (By.CSS_SELECTOR, "[data-bind*='textInput: PasswordRepeat']")
    save_button = (By.CSS_SELECTOR, ".modalDialog__button.modalDialog__blueButton")
    cancel_button = (By.CSS_SELECTOR, ".modalDialog__button.modalDialog__buttonLink")
    error_message_simple_password = (By.CSS_SELECTOR, '[data-bind="html: ErrorMessagePassword"]')
    error_message_password = (By.CSS_SELECTOR, '[data-bind="html: ErrorMessagePassword"]')
    error_message_login = (By.CSS_SELECTOR, ".validator[data-bind='text: ErrorMessageLogin']")
    login_edit = 'bad_login'
    password = 'password'
    password_new = 'password1234'


    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}Login/#/ChangePasswordPage' # добавка к основному урлу ведущая на cтраницу смены пароля

    @allure.step('Open "Edit" page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Проверка на открытие страницы редактирования данных входа')
    def assert_edit_page_is_opened(self):
        # сделать отдельную функции и ее вызывать
        element = self.get_element(self.edit_page)
        assert element.is_displayed(), f"Element {self.edit_page} is not visible"

    @allure.step('Ввод кредов с простым паролем на странице редактирования данных')
    def enter_cridentials_with_simple_password(self):
        inputs = [
            (self.login_input, self.login_edit),
            (self.password_input, self.password),
            (self.password_new_input, self.password_new),
            (self.repeat_password_new_input, self.password_new)
        ]

        # Заполнение всех полей
        for selector, value in inputs:
            self.fill_input(selector, value)

        self.click_on(self.save_button)

        # отдельная функция get_element (проверять что виден)
        error_message_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_message_simple_password))

        # Выводим фактический текст ошибки для отладки
        actual_error_message = error_message_element.text.strip().replace('\n', ' ')
        
        # print(f"Фактическое сообщение об ошибке: '{actual_error_message}'")

        # Проверка текста ошибки
        expected_error_message = ("Ваш пароль не может быть менее 8 символов. " 
                                  "При создании пароля используйте не менее 3 из 4 разрешенных символов: заглавную букву, "
                                  "маленькую букву, число и специальный символ (! @ # $ % ^ & * ( ) _ - + : ; , . > < = \" ).")

        # Проверка текста ошибки
        assert actual_error_message == expected_error_message, f"Expected: '{expected_error_message}', but got: '{actual_error_message}'"

    @allure.step('Ввод кредов без логина на странице редактирования данных')
    def enter_cridentials_without_login(self):
        inputs = [
            (self.password_input, self.password),
            (self.password_new_input, self.password_new),
            (self.repeat_password_new_input, self.password_new)
        ]
        # Заполнение всех полей
        for selector, value in inputs:
            self.fill_input(selector, value)

        self.click_on(self.save_button)

        error_message_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_message_login))

        # Выводим фактический текст ошибки для отладки
        actual_error_message = error_message_element.text.strip()
        print(f"Фактическое сообщение об ошибке: '{actual_error_message}'")

        expected_error_message = 'Не указано имя пользователя.'
        assert actual_error_message == expected_error_message, (f"Expected: '{expected_error_message}', but got: '{actual_error_message}'")

    @allure.step('Ввод кредов без нового пароля на странице редактирования данных')
    def enter_cridentials_without_new_password(self):
        inputs = [
            (self.login_input, self.login_edit),
            (self.password_input, self.password),
            (self.repeat_password_new_input, self.password_new)
        ]

        # Заполнение всех полей
        for selector, value in inputs:
            self.fill_input(selector, value)

        self.click_on(self.save_button)

        error_message_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_message_password))

        # Выводим фактический текст ошибки для отладки
        actual_error_message = error_message_element.text.strip()
        print(f"Фактическое сообщение об ошибке: '{actual_error_message}'")

        # поместить в отдельный степ

    def assert___()
        expected_error_message = 'Это поле должно быть заполнено'
        assert actual_error_message == expected_error_message, (
            f"Expected: '{expected_error_message}', but got: '{actual_error_message}'")


    @allure.step('Отмена изменений на странице редактирования')
    def сhange_reversal(self):
        inputs = [
            (self.login_input, self.login_edit),
            (self.password_input, self.password),
            (self.password_new_input, self.password_new),
            (self.repeat_password_new_input, self.password_new)
        ]

        # Заполнение всех полей
        for selector, value in inputs:
            self.fill_input(selector, value)

        self.click_on(self.cancel_button)
        login_page = loginPage(self.driver)
        return login_page
