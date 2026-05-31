import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from config import BASE_URL

class TestOrder:

    @allure.feature("Заказ самоката")
    @allure.story("Позитивный флоу оформления заказа")
    @allure.title("Оформление заказа через верхнюю и нижнюю кнопки")
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
        
        # Исправлено: Ожидание URL спрятано в метод базового класса
        assert order_page.wait_for_url_to_be(BASE_URL + "/"), "Логотип 'Самокат' не вернул на главную!"


    @allure.feature("Навигация")
    @allure.title("Клик по логотипу 'Яндекс' перенаправляет на Дзен")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        
        order_page.click_yandex_logo()
        
        # Исправлено: все шаги работы с окнами заменены методами POM
        order_page.wait_for_new_window(current_handles_count=1)
        order_page.switch_to_window(index=1)
        
        is_dzen_loaded = order_page.wait_for_url_contains_any(["dzen.ru", "yandex.ru"])
        assert is_dzen_loaded, "Логотип 'Яндекс' не перенаправил на Дзен!"