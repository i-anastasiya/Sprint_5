import pytest
from selenium import webdriver

from constants import Constants


@pytest.fixture
def driver():
    # фикстура для запуска сайта
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def open_stellar_burgers(driver):
    driver.get(Constants.URL)
    return driver

@pytest.fixture
def registration(driver):
    # фикстура для открытия экрана регистрации
    driver.get(Constants.URL_REGISTRATION)
    return driver

@pytest.fixture
def login(driver):
    # фикстура для открытия экрана авторизации
    driver.get(Constants.URL_LOGIN)
    return driver
