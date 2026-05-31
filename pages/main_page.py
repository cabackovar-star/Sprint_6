import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import BASE_URL

class MainPage(BasePage):
    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step("Кликнуть на вопрос номер {index}")
    def click_question(self, index):
        question_xpath = MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index)
        question_locator = (By.XPATH, question_xpath)
        self.js_scroll_to_element(question_locator)
        self.js_click(question_locator)

    @allure.step("Получить текст ответа номер {index}")
    def get_answer_text(self, index):
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        answer_xpath = MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index)
        answer_locator = (By.XPATH, answer_xpath)
        visible_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(answer_locator))
        return visible_element.text

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.js_scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)