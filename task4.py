#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

dictionary = {'a': 35, 'b': 21, 'c': 11, 'd': 20}
result = 1
for i in dictionary:
    result *= dictionary[i]
print(result)
