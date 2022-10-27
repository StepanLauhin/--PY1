def get_count_char(str_):
    str_ = str_.lower()
    dictionary = {}
    for i in str_:
        if i.isalpha():
            dictionary[i] = dictionary.get(i, 0) + 1
    return dictionary


def get_fraction_char(dict_):
    sum_char = sum(dict_.values())
    for i in dict_:
        dict_[i] = dict_[i] / sum_char * 100
    sum_num = 0
    after_comma = 0
    while True:
        dict_copy = dict_.copy()
        for i in dict_:
            dict_copy[i] = round(dict_[i], after_comma)
        sum_num = sum(dict_copy.values())
        if abs(sum_num-100) < 1 ** (-1 - after_comma):
            break
        after_comma += 1
    return dict_copy


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
# print(get_fraction_char(get_count_char(main_str)))

# Если нужно увидеть процентное содержание каждой буквы, достаточно раскомментировать последнюю строку

