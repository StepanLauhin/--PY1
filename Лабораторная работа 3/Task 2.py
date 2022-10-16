list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_ = 0
# TODO Оформить решение
for i, m in enumerate(list_numbers):
    if m > max_:
        max_ = m
        maxi = i
list_numbers[maxi], list_numbers[-1] = list_numbers[-1], list_numbers[maxi]
print(list_numbers)
