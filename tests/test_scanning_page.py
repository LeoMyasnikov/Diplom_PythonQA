import allure
from pages.login_page import LoginPage
from pages.scanning_page import ScanningPage


@allure.feature('ScanningPage')
class TestScanningPage:
    @allure.story("Проверка открытия страницы сканирования")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_scanning_page(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.assert_scanning_page_is_opened()

    @allure.story("Проверка открытия нужного проекта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_project_choice(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.assert_current_url()

    @allure.story("Проверка корректного отображения параметров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_params(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.open_params()

    @allure.story("Проверка изменения приоритета у пакета")
    @allure.severity(allure.severity_level.NORMAL)
    def test_choice_priority(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.open_params()
        scanning_page.choice_priority()

    @allure.story("Проверка обновления пакетов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_package_update(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.package_update()

    @allure.story("Проверка изменения типа пакета")
    @allure.severity(allure.severity_level.NORMAL)
    def test_change_package_type(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.change_type_package()
        scanning_page.assert_change_type_package()

    @allure.story("Проверка, что пакет создается корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_batch(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.change_type_package()
        scanning_page.create_batch()
        scanning_page.assert_create_batch()

    @allure.story("Проверка на изменение имени пакета")
    @allure.severity(allure.severity_level.NORMAL)
    def test_rename_batch(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.change_type_package()
        scanning_page.create_batch()
        scanning_page.rename_batch()
        scanning_page.assert_rename_batch()

    @allure.story("Проверка на вывод пакетов с определенным именем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_batch_name(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.change_type_package()
        scanning_page.sort_name()
        scanning_page.assert_sort_name()

    @allure.story("Проверка на вывод пакетов, созданных в определенные даты")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_batch_date(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.change_type_package()
        scanning_page.sort_date()
        scanning_page.assert_sort_date()

    @allure.story("Проверка на взятие задачи на пересканирование")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_rescan_task(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.get_task_rescanning()
        scanning_page.assert_get_task_rescanning()

    @allure.story("Проверка на загрузку документа в пакет")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_document(self, driver):
        login_page = LoginPage(driver)
        scanning_page = ScanningPage(driver)
        scanning_page.open_scanning()
        login_page.enter_credentials()
        scanning_page.project_choice()
        scanning_page.create_batch()
        scanning_page.upload_document()
        scanning_page.assert_upload_document()





















