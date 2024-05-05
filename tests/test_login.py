from selenium import webdriver
from data import Login, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestLoginIn:

    # проверка по кнопке «Войти в аккаунт» на главной
    def test_login_in_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.LOGIN_ACC).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        assert driver.find_element(*Locators.CHECKOUT_BUT).is_displayed()

        driver.quit()

    # проверка входа через кнопку «Личный кабинет»
    def test_login_in_from_personal_acc(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        assert driver.find_element(*Locators.CHECKOUT_BUT).is_displayed()

        driver.quit()

    # проверка входа через кнопку в форме регистрации
    def test_login_in_from_registration_form(self):
        driver = webdriver.Chrome()
        driver.get(Url.reg_url)

        driver.find_element(*Locators.LOGIN_REG_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        assert driver.find_element(*Locators.CHECKOUT_BUT).is_displayed()

        driver.quit()

    # проверка входа через кнопку в форме восстановления пароля
    def test_login_in_from_forgot_password_form(self):
        driver = webdriver.Chrome()
        driver.get(Url.forgot_url)

        driver.find_element(*Locators.LOGIN_REG_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        assert driver.find_element(*Locators.CHECKOUT_BUT).is_displayed()

        driver.quit()
