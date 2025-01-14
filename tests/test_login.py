import allure
from pages.login_page import loginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('LoginPage')
class TestLoginPage():

    def test_open_page(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.assert_page_is_opened()

    def test_login(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        # wait = WebDriverWait(driver, 5)
        # wait.until(EC.visibility_of_element_located(login_page.login_field))
        personal_page = login_page.enter_cridentials()
        personal_page.assert_page_is_opened()

    def test_account_lockout(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.enter_incorrect_password()

    def test_edit_password_after_default(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        # no
        edit_page = login_page.enter_default_cridentials()
        edit_page.assert_edit_page_is_opened()

    def test_change_language(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.change_language()

        assert 

    def test_incorrect_login(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.enter_incorrect_login()

    def test_open_help(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.open_help(driver)

    def test_copywrite(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.copywriting_check()








