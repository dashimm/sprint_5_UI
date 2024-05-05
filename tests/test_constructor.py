from selenium import webdriver
from test_data import Login, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestConstructorsTabs:

    # проверка перехода в раздел Соусы
    def test_click_to_sauce_tab(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SPICY_SAUCE))
        assert driver.find_element(*Locators.SPICY_SAUCE).is_displayed()

        driver.quit()

    # проверка перехода в раздел Булочки
    def test_click_to_buns_tab(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.SAUCES_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUN))
        assert driver.find_element(*Locators.BUN).is_displayed()

        driver.quit()

    # проверка перехода в раздел Начинки
    def test_click_to_fillings_tab(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING))
        assert driver.find_element(*Locators.FILLING).is_displayed()

        driver.quit()
