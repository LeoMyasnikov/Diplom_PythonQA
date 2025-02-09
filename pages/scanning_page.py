import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.base import Base
from data.cridentials import DOMAIN


class ScanningPage(Base):

    scanning_page = (By.XPATH, '//div[@class="modalTitle__VuTxy"]')
    params_page = (By.XPATH, '//div[@class="modalTitle__VuTxy"]')
    rescan_page = (By.XPATH, "//div[@class='tabItem__r4ljx']//div[text()='Пересканирование']")
    priority_сhoice = (By.XPATH, f"//div[@class='toggleItem__Bg_1g' and text()='Самый высокий']")
    choice_project = (By.XPATH, '//div[@class="selectTitle__OmThc"]')
    postgre_project = (By.XPATH, '//div[@class="selectOption__ablSb"]')
    button_project_entrance = (By.XPATH, '//div/button[@class="button__z74UG buttonPrimary__EvbyJ"]')
    button_params = (By.CSS_SELECTOR, 'svg[viewBox="0 0 15.525513 16"]')
    button_by_default = (By.CSS_SELECTOR, '[.button__z74UG.buttonLink__QePOQ]')
    button_save_batch_settings = (By.CSS_SELECTOR, '[.button__z74UG.buttonPrimary__EvbyJ]')
    button_package_update = (By.ID, 'Regresh_Button')
    package_list = (By.CSS_SELECTOR, 'div[style*="display: inline-flex"] > div[style*="font-size: 14px"]')
    package_type = (By.XPATH, '//div[@class="selectOption__ablSb"]/div[text()="lev"]')
    package_name_table = (By.XPATH, '//div[@class="tableBodyCellText__erL2q" and text()="lev"]')
    toggle_element = (By.CSS_SELECTOR, 'div.toggleItem__Bg_1g.active__ujpKO')
    name_batch = (By.CSS_SELECTOR, '[class="input__vFbYg"]')
    show_batch_button = (By.CSS_SELECTOR, '[class="button__z74UG buttonSecondary__32o_r"]')

    expected_project_url = 'http://myasnikovhost//ContentCapture/Scanning/Batches?projectId=1'

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}Scanning/' # добавка к основному урлу ведущая на персональную страницу

    @allure.step('Открытие страницы сканирования')
    def open_scanning(self):
        self.driver.get(self.page)

    @allure.step('Убеждаемся, что открылась именно страница сканирования')
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

    def assert_choice_priority(self):
        active_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[@class='toggleItem__Bg_1g active__ujpKO' and text()='Самый высокий']")
            )
        )
        assert active_element is not None, f"Элемент с текстом 'Самый высокий' не стал активным"

    @allure.step('Вовзрат настроек пакета по умолчанию')
    def params_by_default(self):
        self.click_on(self.button_by_default)

    def assert_params_by_default(self):
        # Ожидаемый текст
        expected_text = "Обычный"

        # Проверяем видимость элемента и его текст
        self.element_visibility(self.toggle_element, expected_text)

    @allure.step('Открытие окна с настройками параметров')
    def open_params(self):
        self.click_on(self.button_params)
        assert self.get_element(self.params_page), 'Element is not visible'

    @allure.step('Обновление списка пакетов сканирования')
    def package_update(self):
        self.click_on(self.button_package_update)

    def assert_package_update(self):
        # Ожидаемый текст
        expected_text = 'Показано: с 1 по 2 из 2'
        # Проверяем видимость элемента и его текст
        self.element_visibility(self.package_list, expected_text)

    @allure.step('Смена типа пакета')
    def change_type_package(self):
        self.force_click_on(self.package_type)

    def assert_change_type_package(self):
        self.assert_element_is_visible(self.package_name_table)

    @allure.step('Создание пакета')
    def create_batch(self):
        button_add_batch = (By.XPATH, "//div[text()='Добавить из папки']")
        self.click_on(button_add_batch)

    def assert_create_batch(self):
        element = (By.XPATH, "//div[@class='batchEditorInfo__ZPL5X']")
        expected_text = 'Документы: 0\nСтраницы: 0'
        self.element_visibility(element, expected_text)

    @allure.step('Переименование пакета')
    def rename_batch(self):
        new_name = 'test'
        self.fill_input(self.name_batch, new_name)

    def assert_rename_batch(self):
        expected_text = 'test'
        self.element_visibility(self.name_batch, expected_text)

    @allure.step('Сортировка пакетов по имени')
    def sort_name(self):
        select_name = (By.XPATH, "//div[text()='Пакеты, имена которых начинаются с...']")
        name_field = (By.CSS_SELECTOR, '[class="input__vFbYg"]')
        name = 'Пакет'
        self.force_click_on(select_name)
        self.fill_input(name_field, name)
        self.click_on(self.show_batch_button)

    def assert_sort_name(self):
        batch_name = (By.XPATH, "//div[contains(@class, 'tableBodyCellText__erL2q')]//div[text()='Пакет']")
        self.assert_element_is_visible(batch_name)

    @allure.step('Сортировка по дате создания')
    def sort_date(self):
        locators = {
            "select_name": (By.XPATH, "//div[text()='Пакеты, которые были созданы...']"),
            "date_first_field": (
            By.XPATH, "(//div[@class='react-datepicker-wrapper']//input[@class='datepicker__vh7H_'])[1]"),
            "date_second_field": (
            By.XPATH, "(//div[@class='react-datepicker-wrapper']//input[@class='datepicker__vh7H_'])[2]"),
            "date_first_calendar": (By.CSS_SELECTOR,
                                    '[class="react-datepicker__day react-datepicker__day--003"]'),
            "date_second_calendar": (By.CSS_SELECTOR, '[class="react-datepicker__day react-datepicker__day--005"]')
        }

        # Клик по элементам в последовательности
        actions = [
            locators["select_name"],
            locators["date_first_field"],
            locators["date_first_calendar"],
            locators["date_second_field"],
            locators["date_second_calendar"],
            self.show_batch_button
        ]

        for action in actions:
            self.force_click_on(action)

    def assert_sort_date(self):
        batch_date = (By.XPATH, "//div[contains(text(), '04.02.2025, 12:54:58')]")
        self.assert_element_is_visible(batch_date)

    @allure.step('Взятие задачи на пересканирование')
    def get_task_rescanning(self):
        self.click_on(self.rescan_page)
        batch_name = (By.XPATH, "//div[contains(text(), 'Пакет2')]")
        time.sleep(3) #работает только с time.sleep, почему-то. Хотя в методе click_on есть ожидание EC
        self.click_on(batch_name)

    def assert_get_task_rescanning(self):
        task_name = (By.CSS_SELECTOR, "[class='input__vFbYg']")
        expected_text = 'Пакет2'
        self.element_visibility(task_name, expected_text)

    @allure.step('Загрузка документов в пакет')
    def upload_document(self):
        add_file_element = (By.CSS_SELECTOR, 'input[type="file"]')
        file_path = 'C:/capture/htmlimage.png'
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.display = 'block';",
                                             self.get_element(add_file_element))
        self.fill_input(add_file_element, file_path)

    def assert_upload_document(self):
        element = (By.XPATH, "//div[@class='batchEditorInfo__ZPL5X']")
        expected_text = 'Документы: 1\nСтраницы: 1'
        self.element_visibility(element, expected_text)






















































