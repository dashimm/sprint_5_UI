from selenium import webdriver
from test_data import Login, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestPersonalArea:

    # Проверка перехода по клику на «Личный кабинет»
    def test_click_to_go_to_personal_acc(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUT))
        assert driver.find_element(*Locators.LOGOUT_BUT).is_displayed()

        driver.quit()

    # Переход из личного кабинета по кнопке Конструктор
    def test_click_to_go_to_constructor(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        assert driver.find_element(*Locators.CHECKOUT_BUT).is_displayed()

        driver.quit()

    # Переход из личного кабинета по лого Stellar Burger
    def test_click_to_stellar_burger(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.STELLAR_BURGER_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        assert driver.find_element(*Locators.CHECKOUT_BUT).is_displayed()

        driver.quit()
