bad_data = input('Введите элементы списка через запятую: ')
elements = list(bad_data.replace(';', ' ').replace(',', ' ').replace('/', ' ').split())
print(set(elements))


