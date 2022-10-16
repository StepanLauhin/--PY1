# money_capital = 10000
# salary = 5000
# spend = 6000
# increase = 0.05
#
# month = 0  # количество месяцев, которое можно прожить
#
# # TODO Оформить решение
# while money_capital > 0:
#     money_capital -= spend - salary
#     spend *= 1 + increase
#     if money_capital > 0:
#         month += 1
# print(month)
# По моей логике на траты изначально уходила ЗП, а только потом использовалась ПБ
# Если же мы предположим, что ЗП будет получена только в конце месяца, а траты нужно произвести уже в начале,
# то будет получен заложенный ответ
money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
while money_capital > 0:
    money_capital -= spend
    spend *= 1 + increase
    if money_capital > 0:
        money_capital += salary
        month += 1
print(month)
