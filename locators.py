from selenium.webdriver.common.by import By


class Locators:
    REGISTRATION_BUT = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" на странице
    # регистрации
    NAME_FIELD = (By.XPATH, './/label[text() = "Имя"]/following-sibling::input')  # поле ввода имени на странице
    # регистрации
    EMAIL_FIELD_NEW_USER = (By.XPATH, './/label[text() = "Email"]/following-sibling::input')  # поле ввода логина на
    # странице регистрации
    PASSWORD_FIELD_NEW_USER = (By.XPATH, "//input[@name= 'Пароль']")  # поле ввода пароля на странице регистрации
    ERROR_TEXT = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # текст ошибки "Некорректный пароль" на странице
    # регистрации

    LOGIN_ACC = (By.XPATH, "//button[.= 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    EMAIL_FIELD = (By.NAME, "name")  # поле ввода логина на странице входа в аккаунт
    PASSWORD_FIELD = (By.NAME, "Пароль")  # поле ввода пароля на странице входа в аккаунт
    LOGIN_BUT = (By.XPATH, "//button[text() = 'Войти']")  # кнопка "Войти" на странице входа в аккаунт
    CHECKOUT_BUT = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка "Оформить заказ" на главной странице
    PERSONAL_ACC_BUT = (By.XPATH, "//a[.= 'Личный Кабинет']")  # кнопка "Личный кабинет" на главной странице
    LOGIN_REG_BUT = (By.CLASS_NAME, "Auth_link__1fOlj")  # кнопка "Войти" на страницах возобновления пароля/регистрации

    LOGOUT_BUT = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход" в личном кабинете залогиненого пользователя
    CONSTRUCTOR_BUT = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор" в личном кабинете залогиненого
    # пользователя
    STELLAR_BURGER_BUT = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # кнопка логотипа Stellar Burger в шапке
    # сайта

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # таб для перехода в раздел "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # таб для перехода в раздел "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # таб для перехода в раздел "Начинки"
    BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")  # описание булки, отображаемой при переходе в "Булки"
    SPICY_SAUCE = (By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']")  # описание соуса, отобржаемого
    # при переходе в "Соусы"
    FILLING = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']")  # описание начинки, отображаемой при переходе
    # в "Начинки"
