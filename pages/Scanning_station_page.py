import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.base import Base
from data.credentials import DOMAIN


class ScanningPage(Base):

    scanning_page = (By.XPATH, '//div[@class="modalTitle__VuTxy"]')
    params_page = (By.XPATH, '//div[@class="modalTitle__VuTxy"]')
    priority_сhoice = (By.XPATH, f"//div[@class='toggleItem__Bg_1g' and text()='Самый высокий']")
    choice_project = (By.XPATH, '//div[@class="selectTitle__OmThc"]')
    postgre_project = (By.XPATH, '//div[@class="selectOption__ablSb"]')
    expected_project_url = 'http://myasnikovhost//ContentCapture/Scanning/Batches?projectId=1'
    button_project_entrance = (By.XPATH, '//div/button[@class="button__z74UG buttonPrimary__EvbyJ"]')
    button_params = (By.CSS_SELECTOR, 'svg[viewBox="0 0 15.525513 16"]')
    button_by_default = (By.CSS_SELECTOR, '[.button__z74UG.buttonLink__QePOQ]')
    button_save_batch_settings = (By.CSS_SELECTOR, '[.button__z74UG.buttonPrimary__EvbyJ]')
    button_package_update = (By.ID, 'Regresh_Button')
    package_list = (By.CSS_SELECTOR, 'div[style*="display: inline-flex"] > div[style*="font-size: 14px"]')
    package_type = (By.XPATH, '//div[@class="selectOption__ablSb"]/div[text()="lev"]')
    package_name_table = (By.XPATH, '//div[@class="tableBodyCellText__erL2q" and text()="lev"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}Scanning/' # добавка к основному урлу ведущая на персональную страницу

    @allure.step('Assert scanning page is open')
    def assert_scanning_page_is_opened(self):
       assert self.get_element(self.scanning_page), 'Element is not visible'

    @allure.step('Выбор определенного проекта')
    def project_choice(self):
        self.click_on(self.choice_project)
        self.click_on(self.postgre_project)
        self.click_on(self.button_project_entrance)

    @allure.step('Проверка, что после выбора проекта открылась страница с нужным проектом')
    def assert_current_url(self):
        self.driver.implicitly_wait(7)
        current_url = self.driver.current_url
        if current_url == self.expected_project_url:
            print("URL соответствует ожидаемому:", current_url)
        else:
            print("URL не соответствует. Ожидался:", self.expected_project_url, "Получен:", current_url)

    @allure.step('Выбор приоритета в параметрах пакета')
    def choice_priority(self):
        self.click_on(self.priority_сhoice)
        active_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[@class='toggleItem__Bg_1g active__ujpKO' and text()='Самый высокий']")
            )
        )
        assert active_element is not None, f"Элемент с текстом 'Самый высокий' не стал активным"

    @allure.step('Вовзрат настроек пакета по умолчанию')
    def params_by_default(self):
        self.click_on(self.button_by_default)

        toggle_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.toggleItem__Bg_1g.active__ujpKO'))
        )

        # # Получение текста элемента
        # actual_text = toggle_item.text

        # # Проверка, что текст соответствует ожидаемому
        # assert actual_text == "Обычный", f"Expected 'Обычный', but got '{actual_text}'"

        # print("Тест пройден: элемент отображается с правильным текстом.")

    @allure.step('Открытие окна с настройками параметров')
    def open_params(self):
        self.click_on(self.button_params)
        assert self.get_element(self.params_page), 'Element is not visible'

    @allure.step('Обновление списка пакетов сканирования')
    def package_update(self):
        self.click_on(self.button_package_update)
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.package_list))
        element_text = element.text
        assert element_text == 'Показано: с 1 по 2 из 2', f"Expected 'Обычный', but got '{element_text}'"
        # print("Пройдено")

    @allure.step('Смена типа пакета')
    def change_type_package(self):
        self.force_click_on(self.package_type)
        assert self.get_element(self.package_name_table), 'Element is not visible' #ищем значение измененного типа в таблице

    # core
    def assert_that_element_has_text(locator, text):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator))
        element_text = element.text
        assert element_text == text, f"Expected '{text}', but got '{element_text}'"


























