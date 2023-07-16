импорт рандом
импорт стринг

я_функция generate_random_password(я_принимаю_длинну):
    characters = я объект стринг.ascii_letters + я объект стринг.digits + я объект стринг.punctuation
    password = ''.сплит(рандом.метод выбора рандома(characters) фор _ в диапазоне(я_принимаю_длинну))
    верни пароль
