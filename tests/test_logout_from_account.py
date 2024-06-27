from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestStellarBurgersAccount:
    def tests_go_personal_account(self, open_stellar_burgers):
        # Выход из аккаунта
        # Проверь выход по кнопке «Выйти» в личном кабинете.
        open_stellar_burgers.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        open_stellar_burgers.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        open_stellar_burgers.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        open_stellar_burgers.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(open_stellar_burgers, 5).until(EC.visibility_of_element_located
                                                     ((Locators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        # Проверяем также переход в Личный кабинет
        open_stellar_burgers.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        assert open_stellar_burgers.find_element(*Locators.BUTTON_EXIT).text == 'Выход'
        # Выходим из аккаунта
        open_stellar_burgers.find_element(*Locators.BUTTON_EXIT).click()
        title = WebDriverWait(open_stellar_burgers, 5).until(EC.visibility_of_element_located
                                               ((Locators.REGISTRATION_BUTTON))).text
        assert title == 'Зарегистрироваться'
