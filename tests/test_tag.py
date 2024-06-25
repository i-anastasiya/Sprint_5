from locators import Locators


class TestStellarBurgers:
    def tests_tags(self, driver):
        driver.find_element(*Locators.TAG_2).click()
        assert driver.find_element(*Locators.TITLE_2).text == 'Соусы'
        driver.find_element(*Locators.TAG_3).click()
        assert driver.find_element(*Locators.TITLE_3).text == 'Начинки'
        driver.find_element(*Locators.TAG_1).click()
        assert driver.find_element(*Locators.TITLE_1).text == 'Булки'
