from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

faker = Faker()


class TestStellarBurgers:
    def tests_registration(self, driver_registration):
        # Успешная регистрация
        email = faker.email()
        password = 123456
        name = 'Ivan'
        driver_registration.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        driver_registration.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        driver_registration.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(password)
        driver_registration.find_element(*Locators.AUTH_BUTTON).click()
        # Добавляю ожидание, чтобы прогрузился следующий экран авторизации
        WebDriverWait(driver_registration, 5)
        driver_registration.find_element(*Locators.EMAIL).send_keys(name)
        driver_registration.find_element(*Locators.PASSWORD).send_keys(email)
        driver_registration.find_element(*Locators.AUTH_BUTTON).click()
        name_button = WebDriverWait(driver_registration, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                        '//*[@id="root"]/div/main/section[2]/div/button'))).text
        assert name_button == 'Оформить заказ'

    def tests_registration_error(self, driver_registration):
        # Регистрация. Ошибка для некорректного пароля.
        email = faker.email()
        password = 12345
        name = 'Ivan'
        driver_registration.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        driver_registration.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        driver_registration.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(password)
        driver_registration.find_element(*Locators.AUTH_BUTTON).click()
        assert driver_registration.find_element(*Locators.INCORRECT_PASSWORD).text == 'Некорректный пароль'
