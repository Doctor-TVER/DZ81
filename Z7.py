'''
Задача 7
Найти произведение цифр числа.
    Пример:
    254314
    Произведение цифр числа - 480(2*5*4*3*1*4)
'''
n = 254314
number = list(map(int, str(n)))
my_sum = 1
for i in number:
    my_sum *=i
print(my_sum)