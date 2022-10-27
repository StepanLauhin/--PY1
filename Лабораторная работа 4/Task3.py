def delete(list_, index=-1):
    if index == -1:
        return list_[:-1]
    elif index + 1 > len(list_) or abs(index) > len(list_):
        return "ВЫ ПРОСИТЕ УДАЛИТЬ НЕСУЩЕСТВУЮЩИЙ ИНДЕКС"
    else:
        return list_[:index] + list_[index + 1:]


print(delete([0, 0, 1, 2]))  # [0, 0, 1]
print(delete([0, 1, 1, 2, 3], index=-1))  # [0, 1, 1, 2]
print(delete([0, 1, 2, 3, 4, 4], index=-3))  # [0, 1, 2, 4, 4]
print(delete([0, 1, 1, 2, 3], index=-5))  # [1, 1, 2, 3]
print(delete([0, 1, 1, 2, 3], index=-6))  # ВЫ ПРОСИТЕ УДАЛИТЬ НЕСУЩЕСТВУЮЩИЙ ИНДЕКС
print(delete([0, 1, 1, 2, 3], index=5))  # ВЫ ПРОСИТЕ УДАЛИТЬ НЕСУЩЕСТВУЮЩИЙ ИНДЕКС
print(delete([0, 1, 1, 2, 3], index=3))  # [0, 1, 1, 3]
