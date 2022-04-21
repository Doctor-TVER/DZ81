'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6
Найти сумму цифр числа.
    Пример:
    254314
    Сумма цифр числа - 19(2+5+4+3+1+4)
'''
# def digitize(n):
#   return list(map(int, str(n)))

n = 254314
number = list(map(int, str(n)))
# number = digitize(254314)
my_sum = 0
for i in number:
    my_sum +=i
print(my_sum)
