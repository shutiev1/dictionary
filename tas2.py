#Значениями словаря могут быть и списки.
#Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
#Выведите первое и последнее значения каждого из ключей.

dic = dict(zip(['BMW','Tesla'], ['m5', 's', 'x6']))
print(dic.values())