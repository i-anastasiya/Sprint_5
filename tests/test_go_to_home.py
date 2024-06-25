from locators import Locators


class TestStellarBurgers:
    def tests_open_home(self, driver_login):
        # Переход из личного кабинета в конструктор
        # Проверь переход по клику на «Конструктор»
        driver_login.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        assert driver_login.find_element(*Locators.TEXT_HOME).text == 'Соберите бургер'

    def tests_open_home_logo(self, driver_login):
        # Переход из личного кабинета в конструктор
        # Проверь переход по клику на логотип Stellar Burgers
        driver_login.find_element(*Locators.LOGO).click()
        assert driver_login.find_element(*Locators.TEXT_HOME).text == 'Соберите бургер'
