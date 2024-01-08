import random
import string


def random_generator(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


name = random_generator(9)
email = random_generator(9)+'@yandex.ru'
password = random_generator(9)
