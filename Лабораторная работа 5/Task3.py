from random import randint


def get_unique_list_numbers(start: int = -10, finish: int = 10, list_size: int = 15) -> list[int]:
    if not isinstance(start, int) or not isinstance(finish, int) or not isinstance(list_size, int):
        raise TypeError("Все входные аргументы функции должны быть типа int")
    if len(list(range(start, finish+1))) < list_size:
        raise ValueError("Размер списка больше диапазона уникальных целых чисел")
    list_ = []
    while True:
        list_.append(randint(start, finish))
        if len(set(list_)) == list_size:
            return list(set(list_))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
