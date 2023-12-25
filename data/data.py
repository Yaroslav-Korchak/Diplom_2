class Links:
    register_url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    user_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    login_url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    order_url = 'https://stellarburgers.nomoreparties.site/api/orders'


class UserWithoutRequiredFields:
    no_name = {"email": "milleniumfalcon@yandex.ru", "password": "3cipio"}
    no_email = {"password": "3cipio", "name": "Chubaka"}
    no_password = {"email": "milleniumfalcon@yandex.ru", "name": "Chubaka"}
    empty_name = {"name": "", "email": "milleniumfalcon@yandex.ru", "password": "3cipio"}
    empty_email = {"email": "", "password": "3cipio", "name": "Anyname"}
    empty_password = {"email": "milleniumfalcon@yandex.ru", "password": "", "name": "Chubaka"}


