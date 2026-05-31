from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button")
    QUESTION_LOCATOR_TEMPLATE = ".//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR_TEMPLATE = ".//div[@id='accordion__panel-{}']"