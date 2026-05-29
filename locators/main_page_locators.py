from selenium.webdriver.common.by import By

class MainPageLocators:
    # Главная страница Самоката
    URL = "https://qa-scooter.praktikum-services.ru/"
    
    # Кнопка закрытия плашки куки
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    
    # Кнопки "Заказать"
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button")
    
    # Вопросы и ответы в аккордеоне (базовые локаторы для форматирования строк)
    QUESTION_LOCATOR_TEMPLATE = ".//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR_TEMPLATE = ".//div[@id='accordion__panel-{}']"