import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Открыть страницу заказа по прямому URL")
    def open(self):
        # Исправлено: вынесено в константу и вызывается через базовый класс
        self.open_url(OrderPageLocators.URL)

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
        
        next_btn = self.find_element(OrderPageLocators.NEXT_BUTTON)
        self.driver.execute_script("arguments[0].click();", next_btn)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rent_data(self, date, comment):
        date_field = self.find_element(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENT_PERIOD_OPTION_2_DAYS)
        
        checkbox = self.find_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        self.driver.execute_script("arguments[0].click();", checkbox)
        
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        
        confirm_btn = self.find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", confirm_btn)
        
        yes_btn = self.find_element(OrderPageLocators.YES_BUTTON)
        self.driver.execute_script("arguments[0].click();", yes_btn)

    @allure.step("Проверить появление всплывающего окна об успешном заказе")
    def check_success_popup(self):
        return self.find_element(OrderPageLocators.SUCCESS_POPUP).is_displayed()

    @allure.step("Кликнуть на logo 'Самокат'")
    def click_scooter_logo(self):
        logo = self.find_element(OrderPageLocators.SCOOTER_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)

    @allure.step("Кликнуть на logo 'Яндекс'")
    def click_yandex_logo(self):
        logo = self.find_element(OrderPageLocators.YANDEX_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)