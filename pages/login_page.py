import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from core.base import Base
from data.cridentials import DOMAIN


class LoginPage(Base):

    login_page = (By.XPATH, '//div[@class="modalDialog__dialogTitle"]')
    edit_page = (By.XPATH, "//div[text()='Редактировать данные']")
    login_field = (By.ID, 'userName')
    password_field = (By.ID, 'password')
    button_entrance = (By.CSS_SELECTOR, '[value="Войти"]')
    language_hover = (By.XPATH, "//a[text()='English']")
    error_message_login = (By.CSS_SELECTOR, ".validator[data-bind='text: ErrorMessage']")
    error_message_password = (By.CSS_SELECTOR, ".validator.half_margin_bottom")
    button_help = (By.CSS_SELECTOR, '[href="https://help.contentai.ru/content-capture"]')
    copyright_check = (By.CSS_SELECTOR, "#MainFooter .footer_copyright")

    login = 'admin'
    password = 'password'
    login_test = 'test'
    incorrect_password = 'password1234'
    incorrect_login = 'blabla'
    login_with_default_password = 'bad_login'

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}Login/#/Login' # добавка к основному урлу ведущая на персональную страницу

    @allure.step('Открытие "Login" страницы')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Проверка открытия страницы логина')
    def assert_page_is_opened(self):
        self.assert_element_is_visible(self.login_page)

    @allure.step('Авторизация')
    def enter_credentials(self):
        self.fill_input(self.login_field, self.login)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)

    @allure.step('Ввод дефолтного пароля для проверка запроса смены')
    def enter_default_credentials(self):
        self.fill_input(self.login_field, self.login_with_default_password)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)

    @allure.step('Авторизация с некорректным паролем')
    def enter_incorrect_password(self):
        self.fill_input(self.login_field, self.login_test)
        self.fill_input(self.password_field, self.incorrect_password)
        for _ in range(5):
            self.click_on(self.button_entrance)
            time.sleep(2)  # Небольшая пауза между попытками, чтобы избежать проблем с загрузкой

    def assert_incorrect_password(self):
        error_message_element = self.element_visibility(self.error_message_password)
        assert error_message_element.text == "Учетная запись заблокирована", "Ошибка: сообщение об ошибке не совпадает"

    @allure.step('Смена языка')
    def change_language(self):
        self.force_click_on(self.language_hover)

    def assert_change_language(self):
        assert self.driver.title == 'Log In to ContentCapture'

    @allure.step('Ввод неверного логина')
    def enter_incorrect_login(self):
        self.fill_input(self.login_field, self.incorrect_login)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)

    def assert_incorrect_login(self):
        expected_error_message = 'Неверное имя пользователя или пароль.'
        self.element_visibility(self.error_message_login, expected_error_message)

    @allure.step('Открытие справки в новом окне')
    def open_help(self):
        self.click_on(self.button_help)
        self.switch_new_window()

    def assert_open_help(self):
        help_name = 'Справка ContentCapture®'
        assert self.driver.title == help_name

    @allure.step('Проверка копирайта')
    def copyrighting_check(self):
        expected_text = "ContentCapture © ООО «Контент ИИ», 2025"
        self.element_visibility(self.copyright_check, expected_text)
















