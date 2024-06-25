from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestStellarBurgers:
    def tests_go_personal_account(self, driver):
        # Выход из аккаунта
        # Проверь выход по кнопке «Выйти» в личном кабинете.
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                        '//*[@id="root"]/div/main/section[2]/div/button'))).text
        assert name_button == 'Оформить заказ'
        # Проверяем также переход в Личный кабинет
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        assert driver.find_element(*Locators.BUTTON_EXIT).text == 'Выход'
        # Выходим из аккаунта
        driver.find_element(*Locators.BUTTON_EXIT).click()
        # assert driver.find_element(*Locators.TEXT_LOGIN).text == 'Вход'
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                    '//*[@id="root"]/div/main/div/div/p[1]/a'))).text
        assert title == 'Зарегистрироваться'
