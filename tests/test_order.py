import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators

# Исправлено: тест-кейсы находятся строго внутри тестового класса
class TestOrder:

    @allure.feature("Заказ самоката")
    @allure.story("Позитивный флоу оформления заказа")
    @allure.title("Оформление заказа через верхнюю и нижнюю кнопки") # Исправлено: добавлено название allure.title
    @pytest.mark.parametrize(
        "button_type, name, surname, address, phone, date, comment",
        [
            ("top", "Алексей", "Смирнов", "г. Москва, ул. Новая, д. 5", "79998887766", "28.05.2026", "Позвонить за час"),
            ("bottom", "Дмитрий", "Кузнецов", "г. Москва, пр. Мира, д. 12", "79112223344", "01.06.2026", "Оставить у двери")
        ]
    )
    def test_order_scooter(self, driver, button_type, name, surname, address, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        # Исправлено: убран time.sleep(1)
        
        if button_type == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()
            
        order_page.fill_user_data(name, surname, address, phone)
        order_page.fill_rent_data(date, comment)
        
        assert order_page.check_success_popup(), "Окно успешного оформления заказа не появилось!"

    @allure.feature("Навигация")
    @allure.title("Клик по логотипу 'Самокат' возвращает на главную")
    def test_click_scooter_logo_redirects_to_main_page(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        
        order_page.click_scooter_logo()
        
        assert driver.current_url == MainPageLocators.URL, "Логотип 'Самокат' не вернул на главную страницу!"

    @allure.feature("Навигация")
    @allure.title("Клик по логотипу 'Яндекс' перенаправляет на Дзен")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        
        order_page.click_yandex_logo()
        
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        
        WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url)
        
        assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url, "Логотип 'Яндекс' не перенаправил на Дзен!"