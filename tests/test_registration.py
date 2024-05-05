from selenium import webdriver
from test_data import Login, RandomLogin, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestRegistration:

    # проверка успешной регистрации пользователя
    def test_registration(self):
        driver = webdriver.Chrome()
        driver.get(Url.reg_url)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUT))
        driver.find_element(*Locators.NAME_FIELD).send_keys(RandomLogin.name)
        driver.find_element(*Locators.EMAIL_FIELD_NEW_USER).send_keys(RandomLogin.email)
        driver.find_element(*Locators.PASSWORD_FIELD_NEW_USER).send_keys(RandomLogin.password)
        driver.find_element(*Locators.REGISTRATION_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUT))
        assert driver.find_element(*Locators.LOGIN_BUT).is_displayed()

        driver.quit()

    # проверка, что пользователь с некорректным паролем не регистрируется
    def test_not_registration_with_invalid_password(self):
        driver = webdriver.Chrome()
        driver.get(Url.reg_url)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUT))
        driver.find_element(*Locators.NAME_FIELD).send_keys(RandomLogin.name)
        driver.find_element(*Locators.EMAIL_FIELD_NEW_USER).send_keys(RandomLogin.email)
        driver.find_element(*Locators.PASSWORD_FIELD_NEW_USER).send_keys(Login.invalid_password)
        driver.find_element(*Locators.REGISTRATION_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ERROR_TEXT))
        assert driver.find_element(*Locators.ERROR_TEXT).text == 'Некорректный пароль'

        driver.quit()
