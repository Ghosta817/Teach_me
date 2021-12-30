"""                                                 Занятие 1

dict_replace = ['+', '(', ')', '-', ' ']
dict_tell = list()
for _ in range(4):
    tel_number = input().strip()
    for symbol in dict_replace:
        tel_number = tel_number.replace(symbol, '')
    if len(tel_number) == 11:
        tel_number = tel_number[1:]
    elif len(tel_number) == 7:
        tel_number = '495' + tel_number
    dict_tell.append(tel_number)

for tel_num in dict_tell[1:]:
    if tel_num == dict_tell[0]:
        print('YES')
    else:
        print('NO')


a, b, c = [int(input()) for i in range(3)]

if c < 0:
    print('NO SOLUTION')
elif a == 0:
    print('MANY SOLUTIONS')
else:
    answ = []
    for x in range(-10000, 10001):
        if c == (a * x + b) ** 0.5:
            answ.append(x)
        answ.sort()
    if answ:
        print(*answ, sep='\n')
    else:
        print('NO SOLUTION')


a, b, c = [int(input()) for i in range(3)]  # Рабочее решение

if c < 0:
    print('NO SOLUTION')
elif a == 0 and (b ** 0.5 == c):
    print('MANY SOLUTIONS')
else:
    counter = 0
    for x in range(-10000, 10000):
        if (a * x + b) < 0:
            continue
        elif c == (a * x + b) ** 0.5:
            print(x)
            counter += 1
    if counter == 0:
        print('NO SOLUTION')


a, b, c = [int(input()) for i in range(3)]  # Не рабочее решение!

if c < 0:
    print('NO SOLUTION')
elif a == 0 and (b ** 0.5 == c):
    print('MANY SOLUTIONS')
elif a == 0 and (b ** 0.5 != c):
    print('NO SOLUTION')
else:
    x = (c ** 2 - b) / a
    if (a * x + b) < 0:
        print('NO SOLUTION')
    else:
        print(int(x))
"""
from math import ceil

k1, m, k2, p2, n2 = [int(x) for x in input().split()]

k_per_floor = ceil(k2 / n2)
p1 = ceil((k1 / k_per_floor) / m)
n1 = ceil((k1 / k_per_floor) % m)



print(p1, n1)

