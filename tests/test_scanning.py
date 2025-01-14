import allure
from pages.login_page import loginPage

@allure.feature('ScanningPage')
class TestScanningPage():

    def test_open_scanning_page(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.assert_scanning_page_is_opened()

    def test_project_choice(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.project_choice()
        scanning_page.assert_current_url()

    def test_open_params(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.project_choice()
        scanning_page.open_params()

    def test_choice_priority(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.project_choice()
        scanning_page.open_params()
        scanning_page.choice_priority()

    def test_package_update(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.project_choice()
        scanning_page.package_update()

    def test_change_package_type(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.project_choice()
        scanning_page.change_type_package()















