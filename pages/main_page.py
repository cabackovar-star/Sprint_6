import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.driver.get(MainPageLocators.URL)

    @allure.step("Кликнуть на вопрос номер {index}")
    def click_question(self, index):
        question_xpath = MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index)
        question_locator = (By.XPATH, question_xpath)
        self.scroll_to_element(question_locator)
        self.click(question_locator)

    @allure.step("Получить текст ответа номер {index}")
    def get_answer_text(self, index):
        answer_xpath = MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index)
        answer_locator = (By.XPATH, answer_xpath)
        return self.find_element(answer_locator).text

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)