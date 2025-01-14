import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from core.base import Base
from data.cridentials import DOMAIN
from selenium.webdriver.support import expected_conditions as EC


class EditPage(Base):

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
        self.page = f'{DOMAIN}Login/#/ChangePasswordPage'  # добавка к основному урлу ведущая на cтраницу смены пароля

    @allure.step('Open "Edit" page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Проверка на открытие страницы редактирования данных входа')
    def assert_edit_page_is_opened(self):
        edit_page = (By.CSS_SELECTOR, '[class="modalDialog__dialogTitle"]')
        expected_text = 'Редактировать данные'
        self.element_visibility(edit_page, expected_text)

    @allure.step('Ввод кредов с простым паролем на странице редактирования данных')
    def enter_credentials_with_simple_password(self):
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

    def assert_error_simple_password(self):

        # Проверка текста ошибки
        expected_error_message = ("Ваш пароль не может быть менее 8 символов.\n"
                                  "При создании пароля используйте не менее 3 из 4 разрешенных символов: заглавную букву, "
                                  "маленькую букву, число и специальный символ (! @ # $ % ^ & * ( ) _ - + : ; , . > < = \" ).")

        self.element_visibility(self.error_message_simple_password, expected_error_message)

    @allure.step('Ввод кредов без логина на странице редактирования данных')
    def enter_credentials_without_login(self):
        inputs = [
            (self.password_input, self.password),
            (self.password_new_input, self.password_new),
            (self.repeat_password_new_input, self.password_new)
        ]
        # Заполнение всех полей
        for selector, value in inputs:
            self.fill_input(selector, value)

        self.click_on(self.save_button)

    def assert_error_without_login(self):
        expected_error_message = 'Не указано имя пользователя.'
        self.element_visibility(self.error_message_login, expected_error_message)

    @allure.step('Ввод кредов без нового пароля на странице редактирования данных')
    def enter_credentials_without_new_password(self):
        inputs = [
            (self.login_input, self.login_edit),
            (self.password_input, self.password),
            (self.repeat_password_new_input, self.password_new)
        ]

        # Заполнение всех полей
        for selector, value in inputs:
            self.fill_input(selector, value)

        self.click_on(self.save_button)

    def assert_error_without_new_password(self):
        expected_error_message = ("Это поле должно быть заполнено")
        self.element_visibility(self.error_message_password, expected_error_message)

    @allure.step('Отмена изменений на странице редактирования')
    def change_reversal(self):
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
