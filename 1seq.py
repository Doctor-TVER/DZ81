elements = int(input('Введите количество элементов: '))
number = []
for i in range(1,elements+1):
    num = int(input('Введите цифру ' + str(i) + ': '))
    number.append(num)
print(sorted(number))
