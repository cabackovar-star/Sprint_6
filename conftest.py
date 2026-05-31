import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Настройка и запуск браузера Firefox
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    
    yield driver
    
    # Закрытие браузера после окончания теста
    driver.quit()