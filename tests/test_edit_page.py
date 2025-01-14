import allure
from pages.Edit_page import EditPage


@allure.feature('EditPage')
class TestLoginPage():

    def test_open_edit_page(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.assert_edit_page_is_opened()

    def test_simple_password_verification(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.assert_edit_page_is_opened()
        edit_page.enter_cridentials_with_simple_password()

    def test_without_login_verification(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.assert_edit_page_is_opened()
        edit_page.enter_cridentials_without_login()

    def test_without_password_verification(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        edit_page.assert_edit_page_is_opened()
        edit_page.enter_cridentials_without_new_password()

    def test_сhange_reversal(self, driver):
        edit_page = EditPage(driver)
        edit_page.open()
        login_page = edit_page.сhange_reversal()
        login_page.assert_page_is_opened()







