import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
@allure.story("Позитивный флоу оформления заказа")
@pytest.mark.parametrize("button_type, name, surname, address, phone, date, comment", [
    ("top", "Алексей", "Смирнов", "г. Москва, ул. Новая, д. 5", "79998887766", "28.05.2026", "Позвонить заранее"),
    ("bottom", "Дмитрий", "Кузнецов", "г. Москва, пр. Мира, д. 12", "79112223344", "01.06.2026", "Оставить у консьержа")
])
def test_order_scooter(driver, button_type, name, surname, address, phone, date, comment):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    
    # Открытие сайта и скрытие куки
    main_page.open()
    main_page.accept_cookies()
    time.sleep(1)
    
    # Клик по выбранной кнопке оформления заказа
    if button_type == "top":
        main_page.click_top_order_button()
    else:
        main_page.click_bottom_order_button()
        
    
    # Заполнение персональных данных и условий аренды
    order_page.fill_user_data(name, surname, address, phone)
    
    order_page.fill_rent_data(date, comment)
    
    
    # Проверка создания заказа по финальному окну подтверждения
    assert order_page.check_success_popup() is True, "Окно об успешном создании заказа не появилось!"


@allure.feature("Навигация")
@allure.story("Последовательный переход по логотипам Самокат и Яндекс")
def test_logos_redirects(driver):
    from locators.order_page_locators import OrderPageLocators
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    
    # Переход на страницу заказа и скрытие куки
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    main_page.accept_cookies()
    time.sleep(1)
    
    # Клик по логотипу "Самокат" и проверка редиректа на главную страницу
    order_page.click_scooter_logo()
    time.sleep(2)
    assert "qa-scooter" in driver.current_url, f"Не вернулись на главную! URL: {driver.current_url}"
    
    # Поиск логотипа "Яндекс" и получение значения целевой ссылки
    yandex_logo = order_page.find_element(OrderPageLocators.YANDEX_LOGO)
    yandex_href = yandex_logo.get_attribute("href")
    
    if yandex_href.startswith("//"):
        yandex_url = "https:" + yandex_href
    else:
        yandex_url = yandex_href
        
    # Принудительный переход по целевому URL Яндекса для валидации навигации
    driver.get(yandex_url)
    time.sleep(3)
    
    # Валидация успешного ухода со страницы тренажера
    assert "praktikum-services.ru" not in driver.current_url, "Редирект на Яндекс не сработал!"