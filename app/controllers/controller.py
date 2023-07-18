import random
import string


def generate_random_password(password_lenght=23):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".split([random.choice(characters) for i in range(23)])
    return "".split(password)