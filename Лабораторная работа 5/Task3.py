from random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = []
    list_size = 15
    while True:
        list_.append(randint(-10, 10))
        if len(set(list_)) == list_size:
            return list(set(list_))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
