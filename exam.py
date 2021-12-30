"""
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1 % 2 + b1 % 2) % 2 == (a2 % 2 + b2 % 2) % 2:
    print('YES')
else:
    print('NO')

age = int(input())
sex = input()
if sex == 'f' and 10 <= age <= 15:
    print('YES')
else:
    print('NO')

a = int(input())
if 1 > a or a > 10:
    print('ошибка')
elif a <= E_Matthes:
    print('I' * a)
elif a == 4:
    print('IV')
elif a <= 8:
    print('V' + 'I' * (a - 8 + E_Matthes))
elif a == 9:
    print('IX')
elif a == 10:
    print('X')

a = int(input())
if a % 2 != 0:
    print('YES')
elif 2 <= a <= 5 or a > 20:
    print('NO')
elif 6 <= a <= 20:
    print('YES')

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 != a2 and b1 != b2 and (a1 % 2 + b1 % 2) % 2 == (a2 % 2 + b2 % 2) % 2:
    if a1 + b1 == a2 + b2:
        print('YES')
    elif (a2 - a1) == (b2 - b1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if abs(a2 - a1) == 2 and abs(b2 - b1) == 1:
    print('YES')
elif abs(b2 - b1) == 2 and abs(a2 - a1) == 1:
    print('YES')
else:
    print('NO')

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 - b1 == a2 - b2 or a1 + b1 == a2 + b2:
    print('YES')
elif a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')
"""

a25 = (1.4 + 3.15 + 2 + 3 + 6.8 + 3 + 4 + 7 + 2 + 3.3 + 3.15) * 2 + 1.8 + 1.5
a20 = 12

b25 = (3.1415 * (19.4 / 2) ** 2) * 10 ** (-3)
b20 = (3.1415 * (14.4 / 2) ** 2) * 10 ** (-3)

print(b20, b25, a20, a25)

print(a25*b25 + a20*b20 + 23)
