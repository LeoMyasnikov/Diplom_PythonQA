from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_element(self, selector):
        return self.driver.find_element(*selector) # поскольку используется несколько типов локаторов, то передаем selector

    def assert_element_is_visible(self, selector):
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    def element_visibility(self, selector, text, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(selector),
            message=f"Element with locator {selector} is not visible within {timeout} seconds"
        )

        # Получение текста элемента
        element_text = element.text.strip()

        if not element_text:
            element_text = element.get_attribute("value").strip()

            # Проверка текста элемента
        assert element_text == text, f"Expected '{text}', but got '{element_text}'"

        # Возвращаем элемент, если он видим и текст совпадает
        return element

    def fill_input(self, selector, value):
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(selector)
        )
        element = self.get_element(selector)
        element.clear()
        element.send_keys(value)

    def click_on(self, selector):
        # Ожидание, пока элемент станет кликабельным
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(selector)
        )
        # Получение элемента и клик
        element = self.get_element(selector)
        element.click()

    def force_click_on(self, selector):
        element = self.get_element(selector)
        self.driver.execute_script("arguments[0].click();", element)

    def switch_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def upload_files(self, selector, path):
        self.click_on(selector)
        self.fill_input()



