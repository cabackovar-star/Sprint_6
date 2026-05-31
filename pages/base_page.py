import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL браузера")
    def get_current_url(self):
        # Исправлено: тест не обращается к драйверу напрямую, а вызывает этот метод
        return self.driver.current_url

    @allure.step("Ожидание и поиск элемента")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору: {locator}"
        )

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Кликнуть на элемент принудительно через JavaScript")
    def js_click(self, locator):
        # Исправлено: все вызовы execute_script скрыты внутри базового класса
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Проскроллить экран до элемента через JavaScript")
    def js_scroll_to_element(self, locator):
        # Исправлено: скролл перенесен в base_page
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Дождаться, пока URL станет строго равен ожидаемому")
    def wait_for_url_to_be(self, expected_url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))

    @allure.step("Дождаться, пока откроется новая вкладка")
    def wait_for_new_window(self, current_handles_count=1, time=10):
        WebDriverWait(self.driver, time).until(lambda d: len(d.window_handles) > current_handles_count)

    @allure.step("Переключиться на вкладку по индексу")
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Дождаться, пока в URL появится одна из ключевых фраз")
    def wait_for_url_contains_any(self, partial_urls, time=10):
        return WebDriverWait(self.driver, time).until(
            lambda d: any(part in d.current_url for part in partial_urls)
        )

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