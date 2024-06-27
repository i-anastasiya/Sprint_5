from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestStellarBurgersLogin:
    def tests_login_personal_area(self, open_stellar_burgers):
        # вход через кнопку «Личный кабинет» и возвращение в него авторизованным пользователем
        open_stellar_burgers.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        open_stellar_burgers.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        open_stellar_burgers.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        open_stellar_burgers.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(open_stellar_burgers, 5).until(EC.visibility_of_element_located
                                                     ((Locators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'

    def test_login_to_account(self, open_stellar_burgers):
        # вход по кнопке «Войти в аккаунт» на главной
        open_stellar_burgers.find_element(*Locators.COME_IN_BUTTON).click()
        open_stellar_burgers.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        open_stellar_burgers.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        open_stellar_burgers.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(open_stellar_burgers, 5).until(EC.visibility_of_element_located
                                                                   ((Locators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'

    def test_login_password_recovery(self, login):
        # вход через кнопку в форме восстановления пароля.
        login.find_element(*Locators.BUTTON_RECOVERY).click()
        login.find_element(*Locators.BUTTON_LOGIN).click()
        login.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        login.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        login.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(login, 10).until(EC.visibility_of_element_located
                                                     ((Locators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'

    def test_login_registration(self, registration):
        # вход через кнопку в форме регистрации
        registration.find_element(*Locators.BUTTON_LOGIN).click()
        registration.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        registration.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        registration.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(registration, 10).until(EC.visibility_of_element_located
                                                            ((Locators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
