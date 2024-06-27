from locators import Locators


class TestStellarBurgersOpenHome:
    def tests_open_home(self, login):
        # Переход из личного кабинета в конструктор
        # Проверь переход по клику на «Конструктор»
        login.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        assert login.find_element(*Locators.TEXT_HOME).text == 'Соберите бургер'

    def tests_open_home_logo(self, login):
        # Переход из личного кабинета в конструктор
        # Проверь переход по клику на логотип Stellar Burgers
        login.find_element(*Locators.LOGO).click()
        assert login.find_element(*Locators.TEXT_HOME).text == 'Соберите бургер'
