# Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

s = 'pythonist'
dict1 = []
for i in s:
    c = s.count(i)
    dict1.append(c)
a = dict(list(zip(s, dict1)))
print(a)
