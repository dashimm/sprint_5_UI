from selenium import webdriver
from data import Login, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestLogOut:

    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_click_to_logout_from_acc(self):
        driver = webdriver.Chrome()
        driver.get(Url.main_url)

        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Login.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Login.password)
        driver.find_element(*Locators.LOGIN_BUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUT))
        driver.find_element(*Locators.PERSONAL_ACC_BUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUT))
        driver.find_element(*Locators.LOGOUT_BUT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUT))
        assert driver.find_element(*Locators.LOGIN_BUT).is_displayed()

        driver.quit()
