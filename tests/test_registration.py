from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

faker = Faker()


class TestStellarBurgersRegistration:
    def tests_registration(self, registration):
        # Успешная регистрация
        email = faker.email()
        password = 123456
        name = 'Ivan'
        registration.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        registration.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        registration.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(password)
        registration.find_element(*Locators.AUTH_BUTTON).click()
        # Добавляю ожидание, чтобы прогрузился следующий экран авторизации
        WebDriverWait(registration, 5)
        registration.find_element(*Locators.EMAIL).send_keys(name)
        registration.find_element(*Locators.PASSWORD).send_keys(email)
        registration.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(registration, 5).until(EC.visibility_of_element_located
                                                                   ((Locators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'

    def tests_registration_error(self, registration):
        # Регистрация. Ошибка для некорректного пароля.
        email = faker.email()
        password = 12345
        name = 'Ivan'
        registration.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        registration.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        registration.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(password)
        registration.find_element(*Locators.AUTH_BUTTON).click()
        assert registration.find_element(*Locators.INCORRECT_PASSWORD).text == 'Некорректный пароль'
