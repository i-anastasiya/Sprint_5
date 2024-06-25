import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    # фикстура для запуска сайта
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    WebDriverWait(driver_login, 3)
    yield browser

    browser.quit()

@pytest.fixture
def driver_registration():
    # фикстура для открытия экрана регистрации
    browser = webdriver.Chrome()
    browser.get(Constants.URL_REGISTRATION)
    WebDriverWait(driver_registration, 3)
    yield browser

    browser.quit()

@pytest.fixture
def driver_login():
    # фикстура для открытия экрана авторизации
    browser = webdriver.Chrome()
    browser.get(Constants.URL_LOGIN)
    WebDriverWait(driver_login, 3)
    yield browser

    browser.quit()
