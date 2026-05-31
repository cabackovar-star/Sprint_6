import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from config import ORDER_URL

class OrderPage(BasePage):
    @allure.step("Открыть страницу заказа по прямому URL")
    def open(self):
        self.open_url(ORDER_URL)

    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_user_data(self, name, surname, address, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

        metro_field = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys("Черкизовская")
        metro_field.send_keys(Keys.DOWN)
        metro_field.send_keys(Keys.ENTER)

        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.js_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rent_data(self, date, comment):
        date_field = self.find_element(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENT_PERIOD_OPTION_2_DAYS)

        self.js_click(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

        self.js_click(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.js_click(OrderPageLocators.YES_BUTTON)

    @allure.step("Проверить появление всплывающего окна об успешном заказе")
    def check_success_popup(self):
        return self.find_element(OrderPageLocators.SUCCESS_POPUP).is_displayed()

    @allure.step("Кликнуть на logo 'Самокат'")
    def click_scooter_logo(self):
        self.js_click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на logo 'Яндекс'")
    def click_yandex_logo(self):
        self.js_click(OrderPageLocators.YANDEX_LOGO)