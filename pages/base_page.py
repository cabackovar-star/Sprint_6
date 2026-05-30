import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть веб-страницу")
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        # Исправлено: вместо несуществующего presence_of_element_focused используется presence_of_element_located
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
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

    @allure.step("Принять куки, если плашка появилась")
    def accept_cookies(self):
        try:
            from locators.main_page_locators import MainPageLocators
            cookie_btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT_BUTTON)
            )
            cookie_btn.click()
        except:
            pass