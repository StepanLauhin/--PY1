# До того как увидел ожидаемый ответ, составил русский словарь. Решения жалко, поэтому оставил.
# def get_count_char(str_):
#
#     str_ = str_.lower()
#     dictionary = {
#         'а': 0,
#         'б': 0,
#         'в': 0,
#         'г': 0,
#         'д': 0,
#         'е': 0,
#         'ё': 0,
#         'ж': 0,
#         'з': 0,
#         'и': 0,
#         'й': 0,
#         'к': 0,
#         'л': 0,
#         'м': 0,
#         'н': 0,
#         'о': 0,
#         'п': 0,
#         'р': 0,
#         'с': 0,
#         'т': 0,
#         'у': 0,
#         'ф': 0,
#         'х': 0,
#         'ц': 0,
#         'ч': 0,
#         'ш': 0,
#         'щ': 0,
#         'Ъ': 0,
#         'ы': 0,
#         'ь': 0,
#         'э': 0,
#         'ю': 0,
#         'я': 0,
#     }
#
#     for i in str_:
#         if i in dictionary:
#             dictionary[i] += 1
#
#     return dictionary
#
# def get_fraction_char(dict_):
#
#     sum_char = sum(dict_.values())
#
#     for i in dict_:
#         dict_[i] = round(dict_[i] / sum_char * 100, 2)
#
#     return dict_


#
# # TODO посчитать количество каждой буквы в строке в аргументе str_
#
#
# main_str = """
#     Данное предложение будет разбиваться на отдельные слова.
#     В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
#     Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
# """
# print(get_count_char(main_str))
# print(get_fraction_char(get_count_char(main_str)))
# print(sum(get_fraction_char(get_count_char(main_str)).values()))

# А потом подумал, что мог неправильно Вас понять и нужно создавать буквенный словарь для каждой фразы отдельно для
# именно её символов. Тогда так:

def get_count_char(str_):

    str_ = str_.lower()
    dictionary = {}

    for i in sorted(set(str_)):
        if i.isalpha():
            dictionary[i] = 0

    for i in str_:
        if i in dictionary:
            dictionary[i] += 1

    return dictionary


def get_fraction_char(dict_):

    sum_char = sum(dict_.values())

    for i in dict_:
        dict_[i] = round(dict_[i] / sum_char * 100, 2)

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_fraction_char(get_count_char(main_str)))
print(round(sum(get_fraction_char(get_count_char(main_str)).values())))

# Если имелось в виду создать словарь под необходимые символы заранее, то это вариант первый, но плюс-минус буквы из
# фразы. Второй вариант считаю, всё-таки, более универсальным, поэтому привожу его. И мне показалось, что сортированный
# словарь удобнее, поэтому ответ не сходится. Надеюсь, это допустимо

