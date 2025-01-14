import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from core.base import Base
from data.cridentials import DOMAIN
from pages.Personal_page import PersonalPage
from pages.Scanning_station_page import ScanningPage


class loginPage(Base):

    login_page = (By.XPATH, '//div[@class="modalDialog__dialogTitle"]')
    edit_page = (By.XPATH, "//div[text()='Редактировать данные']")
    login_field = (By.ID, 'userName')
    password_field = (By.ID, 'password')
    button_entrance = (By.CSS_SELECTOR, '[value="Войти"]')
    login = 'admin'
    password = 'password'
    login_test = 'test'
    incorrect_password = 'password1234'
    incorrect_login = 'blabla'
    login_with_default_password = 'bad_login'
    language_hover = (By.XPATH, "//a[text()='English']")
    error_message_login = (By.CSS_SELECTOR, ".validator[data-bind='text: ErrorMessage']")
    button_help = (By.CSS_SELECTOR, '[href="https://help.contentai.ru/content-capture"]')
    сopyright_check = (By.CSS_SELECTOR, "#MainFooter .footer_copyright")

    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}Login/#/Login' # добавка к основному урлу ведущая на персональную страницу

        self.page_scanning = f'{DOMAIN}Scanning/'

    @allure.step('Open "Login" page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Open "Scanning" page')
    def open_scanning(self):
        self.driver.get(self.page_scanning)

    @allure.step('Assert this page is open')
    def assert_page_is_opened(self):
       element = self.get_element(self.login_page)
       assert element.is_displayed(), f"Element {self.login_page} is not visible"

    @allure.step('Authorization')
    def enter_cridentials(self):
        self.fill_input(self.login_field, self.login)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)
        personal_page = PersonalPage(self.driver)
        return personal_page

    @allure.step('Ввод дефолтного пароля для проверка запроса смены')
    def enter_default_cridentials(self):
        from Homework_page_object.pages.Edit_page import EditPage #для избегания проблем с инициализацией
        self.fill_input(self.login_field, self.login_with_default_password)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)
        edit_page = EditPage(self.driver)
        return edit_page

    @allure.step('Authorization with incorrect password')
    def enter_incorrect_password(self):
        self.fill_input(self.login_field, self.login_test)
        self.fill_input(self.password_field, self.incorrect_password)
        for _ in range(5):
            self.click_on(self.button_entrance)
            time.sleep(2)  # Небольшая пауза между попытками, чтобы избежать проблем с загрузкой
        error_message_element = self.driver.find_element(By.CSS_SELECTOR, ".validator.half_margin_bottom")
        assert error_message_element.text == "Учетная запись заблокирована", "Ошибка: сообщение об ошибке не совпадает"

    @allure.step('Login with redirect in scanning station')
    def login_in_scanning(self):
        self.fill_input(self.login_field, self.login)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)
        scanning_page = ScanningPage(self.driver)
        return scanning_page

    @allure.step('Сhange language')
    def change_language(self):
        self.force_click_on(self.language_hover)
        time.sleep(7)
        assert self.driver.title == 'Log In to ContentCapture'

    @allure.step('Ввод неверного логина')
    def enter_incorrect_login(self):
        self.fill_input(self.login_field, self.incorrect_login)
        self.fill_input(self.password_field, self.password)
        self.click_on(self.button_entrance)
        error_message_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_message_login))

        # Выводим фактический текст ошибки для отладки
        actual_error_message = error_message_element.text
        print(f"Фактическое сообщение об ошибке: '{actual_error_message}'")

        expected_error_message = 'Неверное имя пользователя или пароль.'
        assert actual_error_message == expected_error_message, (
            f"Expected: '{expected_error_message}', but got: '{actual_error_message}'")

    @allure.step('Открытие справки в новом окне')
    def open_help(self, driver):
        self.click_on(self.button_help)
        self.switch_new_window()

        # Явное ожидание заголовка
        help_name = 'Справка ContentCapture®'
        WebDriverWait(driver, 7).until(EC.title_is(help_name))
        assert driver.title == help_name

    @allure.step('Проверка копирайта')
    def copywriting_check(self):
        footer_copyright = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((self.сopyright_check)))

        actual_text = footer_copyright.text
        expected_text = "ContentCapture © ООО «Контент ИИ», 2024"

        assert actual_text == expected_text, f"Ожидался текст '{expected_text}', но получен '{actual_text}'"
















