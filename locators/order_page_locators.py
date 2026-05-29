from selenium.webdriver.common.by import By

class OrderPageLocators:
    # URL страницы заказа (для проверок)
    URL = "https://qa-scooter.praktikum-services.ru/order"
    
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    
    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.XPATH, ".//div[text()='* Срок аренды']")
    RENT_PERIOD_OPTION_2_DAYS = (By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='двое суток']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    
    # Кнопки подтверждения
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_POPUP = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
    
    # Логотипы в шапке
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")