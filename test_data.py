from random import randint


class Login:
    name = 'Dashima'
    email = 'dashimatsyngueva8321@ya.ru'
    password = '%dashima#'
    invalid_password = '123'


class RandomLogin:
    name = f'Bobr{randint(100, 999)}'
    email = f'bobrkurva{randint(100, 999)}@ya.ru'
    password = f'kurva{randint(100, 999)}!#'


class Url:
    main_url = 'https://stellarburgers.nomoreparties.site'  # главная страница
    log_url = f'{main_url}/login'  # страница входа в лк
    reg_url = f'{main_url}/register'  # страница регистрации
    forgot_url = f'{main_url}/forgot-password'  # страница восстановления пароля
