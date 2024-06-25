from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestStellarBurgers:
    def tests_login_personal_area(self, driver):
        # вход через кнопку «Личный кабинет» и возвращение в него авторизованным пользователем
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                        '//*[@id="root"]/div/main/section[2]/div/button'))).text
        assert name_button == 'Оформить заказ'

    def test_login_to_account(self, driver):
        # вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.COME_IN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                        '//*[@id="root"]/div/main/section[2]/div/button'))).text
        assert name_button == 'Оформить заказ'

    def test_login_password_recovery(self, driver_login):
        # вход через кнопку в форме восстановления пароля.
        driver_login.find_element(*Locators.BUTTON_RECOVERY).click()
        driver_login.find_element(*Locators.BUTTON_LOGIN).click()
        driver_login.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver_login.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver_login.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(driver_login, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                        '//*[@id="root"]/div/main/section[2]/div/button'))).text
        assert name_button == 'Оформить заказ'

    def test_login_registration(self, driver_registration):
        # вход через кнопку в форме регистрации
        driver_registration.find_element(*Locators.BUTTON_LOGIN).click()
        driver_registration.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver_registration.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver_registration.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(driver_registration, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                              '//*[@id="root"]/div/main/section[2]/div/button'))).text
        assert name_button == 'Оформить заказ'
