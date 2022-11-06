from random import sample
import string


def get_random_password(n=8) -> str:
    if not isinstance(n, int):
        raise TypeError(f"У переменной n должен быть тип int, не {type(n)}")
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(sample(alphabet, n))


print(get_random_password())
