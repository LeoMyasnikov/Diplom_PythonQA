import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from core.base import Base
from data.cridentials import DOMAIN


class PersonalPage(Base):

    personal_page = (By.XPATH, '//div[@class="section-header basic_margin_bottom"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    @allure.step('Проверка, что открылась персональная страница')
    def assert_page_is_opened(self):
       assert self.get_element(self.personal_page), 'Element is not visible'















