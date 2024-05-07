from test_data import Url
from locators import Locators
from conftest import driver


class TestConstructorsTabs:

    # проверка перехода в раздел Соусы
    def test_click_to_sauce_tab(self, driver):
        driver.get(Url.main_url)

        driver.find_element(*Locators.SAUCES_TAB).click()
        assert driver.find_element(*Locators.ACTIVE_CONSTRUCTOR_TAB).text == 'Соусы'

    # проверка перехода в раздел Булочки
    def test_click_to_buns_tab(self, driver):
        driver.get(Url.main_url)

        driver.find_element(*Locators.SAUCES_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        assert driver.find_element(*Locators.ACTIVE_CONSTRUCTOR_TAB).text == 'Булки'

    # проверка перехода в раздел Начинки
    def test_click_to_fillings_tab(self, driver):
        driver.get(Url.main_url)

        driver.find_element(*Locators.FILLINGS_TAB).click()
        assert driver.find_element(*Locators.ACTIVE_CONSTRUCTOR_TAB).text == 'Начинки'
