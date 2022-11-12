from random import sample
import string


def get_random_password(password_size=8) -> str:
    if not isinstance(password_size, int):
        raise TypeError("Входной аргумент функции должен быть типа int")
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if password_size > len(alphabet) or password_size < 1:
        raise ValueError(f"Некорректный размер пароля.\n"
                         f" Размер пароля не должен быть больше {len(alphabet)} и меньше 1.")
    return ''.join(sample(alphabet, password_size))


print(get_random_password())
