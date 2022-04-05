
n = 10
xxx = 5
count = 0
for i in range(1,n+1):
    vvod = int(input("Цифра " + str(i) + ": "))
    while vvod > 0:
        if vvod % 10 == xxx:
            count += 1
        vvod = vvod // 10

print("Было введено " + str(count) + " цифр " + str(xxx))