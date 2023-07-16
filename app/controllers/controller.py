import random
from string import ascii_letters, digits, punctuation

def generate_random_password(lenght:int)-> str:
    """Generate random string"""
    characters = str(ascii_letters + digits + punctuation)
    print(characters)
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return  password
