class Links:
    REGISTER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    USER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    LOGIN_URL = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    ORDER_URL = 'https://stellarburgers.nomoreparties.site/api/orders'


class UserWithoutRequiredFields:
    no_name = {"email": "milleniumfalcon@yandex.ru", "password": "3cipio"}
    no_email = {"password": "3cipio", "name": "Chubaka"}
    no_password = {"email": "milleniumfalcon@yandex.ru", "name": "Chubaka"}
    empty_name = {"name": "", "email": "milleniumfalcon@yandex.ru", "password": "3cipio"}
    empty_email = {"email": "", "password": "3cipio", "name": "Anyname"}
    empty_password = {"email": "milleniumfalcon@yandex.ru", "password": "", "name": "Chubaka"}


class TestOrder:
    successful_order = {
  "ingredients": [
    "61c0c5a71d1f82001bdaaa6e",
    "61c0c5a71d1f82001bdaaa76",
    "61c0c5a71d1f82001bdaaa7a",
    "61c0c5a71d1f82001bdaaa74",
    "61c0c5a71d1f82001bdaaa6c"
  ]
}
    bad_order = {"ingredients":  ["bad_ingredient"]}


