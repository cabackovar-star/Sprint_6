from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_focused(locator) if hasattr(EC, 'presence_of_element_focused') else EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору: {locator}"
        )

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def accept_cookies(self):
        try:
            # Ожидание кук до 5 секунд (вызывается только на главной странице в самом начале теста)
            cookie_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT_BUTTON)
            )
            cookie_btn.click()
        except:
            pass