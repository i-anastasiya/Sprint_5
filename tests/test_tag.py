from locators import Locators


class TestStellarBurgersTags:
    def tests_tags_sauces(self, open_stellar_burgers):
        open_stellar_burgers.find_element(*Locators.TAG_2).click()
        assert open_stellar_burgers.find_element(*Locators.TITLE_2).text == 'Соусы'

    def tests_tags_filling(self, open_stellar_burgers):
        open_stellar_burgers.find_element(*Locators.TAG_3).click()
        assert open_stellar_burgers.find_element(*Locators.TITLE_3).text == 'Начинки'

    def tests_tags_buns(self, open_stellar_burgers):
        # сначала проверяем что мы на другом теге, чтобы тапнуть на первый
        open_stellar_burgers.find_element(*Locators.TAG_3).click()
        assert open_stellar_burgers.find_element(*Locators.TITLE_3).text == 'Начинки'
        # теперь проверяем, что именно первый тег тапается
        open_stellar_burgers.find_element(*Locators.TAG_1).click()
        assert open_stellar_burgers.find_element(*Locators.TITLE_1).text == 'Булки'

