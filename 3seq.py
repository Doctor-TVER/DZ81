question_1 = input('Введите элементы 1-го списка через запятую: ')
question_2 = input('Введите элементы 2-го списка через запятую: ')
list_1 = list(question_1.split(','))
list_2 = list(question_2.split(','))
for i in set(list_1) - set(list_2):
    print(i)
