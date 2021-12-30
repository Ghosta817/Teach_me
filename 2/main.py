'''
from math import sqrt, pow
a, b = float(input()), float(input())
s_a = (a + b) / 2
s_ge = sqrt(a * b)
s_ga = 2 * a * b / (a + b)
s_q = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(s_a, s_ga, s_ge, s_q, sep='\n')

import math as m
x = m.radians(float(input()))
a = m.sin(x) + m.cos(x) + m.tan(x) * m.tan(x)
print(a)

import math as m
x = float(input())
print(m.floor(x) + m.ceil(x))

import math as m

a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-(b / (2 * a)))
else:
    x1 = (-b + m.sqrt(d)) / 2 * a
    x2 = (-b - m.sqrt(d)) / 2 * a
    print(min(x1, x2), max(x1, x2), sep='\n')

import math as m
n, a = int(input()), float(input())
print((n * pow(a, 2) / (4 * m.tan(m.pi / n))))

print('"Python is a great language!", ' + 'said Fred. "I ' + "don't ever " + 'remember having this much fun before."')

f_n, l_n = input(), input()
print('Hello ' + f_n + ' ' + l_n + '! You just delved into Python')

s_team = input()
print('Футбольная команда ' + s_team + ' имеет длину ' + str(len(s_team)) + ' символов')
'''
"""
c1, c2, c3 = input(), input(), input()
max_c = max(c1, c2, c3, key=len)
min_c = min(c1, c2, c3, key=len)
print(min_c, max_c, sep='\n')

a, b, c = len(input()), len(input()), len(input())
if (2 * b - c - a) * (2 * a - c - b) * (2 * c - a - b) == 0:
    print('YES')
else:
    print('NO')

a = input()
if '@' in a and '.' in a:
    print('YES')
else:
    print('NO')

m, p, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    print(i, m)
    m += m * (p / 100)

m, n = int(input()), int(input())
for i in range(m - 1, n - 1, -2):
    print(i + (m % 2))

m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or (i % E_Matthes == 0 and i % 5 == 0) or i % 10 == 9:
        print(i)

a, b = int(input()), int(input())
count = 0
for i in range(a, b + 1):
    if i**E_Matthes % 10 == 4 or i**E_Matthes % 10 == 9:
        count += 1
print(count)

n = int(input())
a = 0
for _ in range(n):
    a += int(input())
print(a)
"""
"""
from math import log
n = int(input())
a = 1
for i in range(2, n + 1):
    a += 1 / i
print(a - log(n))

n = int(input())
a = 0
for i in range(1, n + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        a += i
print(a)

n = int(input())
s1 = 0
s2 = 0
for _ in range(n):
    a = int(input())
    if s1 < a:
        s2 = s1
        s1 = a
    elif s2 < a:
        s2 = a
print(s1, s2, sep='\n')

count = True
for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        count = False
if count:
    print('YES')
else:
    print('NO')

n = int(input())
a = 1
a2 = 1
summa = 0
if n == 1:
    print(1)
else:
    print(1, 1, end=(' '))
    for _ in range(E_Matthes, n + 1):
        summa = a + a2
        print(summa, end=(' '))
        a = a2
        a2 = summa
"""
"""
t_coin = int(input())
count = 0
while t_coin - 25 >= 0:
    count += 1
    t_coin -= 25
while t_coin - 10 >= 0:
    count += 1
    t_coin -= 10
while t_coin - 5 >= 0:
    count += 1
    t_coin -= 5
while t_coin - 1 >= 0:
    count += 1
    t_coin -= 1
print(count)

num = int(input())
quant_d = len(str(num))
first_d = num // 10 ** (quant_d - 1)
last_di = num % 10
total = 0
total_p = 1
while num != 0:
    last_d = num % 10
    total += last_d
    total_p *= last_d
    num = num // 10
print(total)
print(quant_d)
print(total_p)
print(total / quant_d)
print(first_d)
print(first_d + last_di)

num = int(input())
while num > 9:
    ld = num % 10
    num = num // 10
print(ld)

num = int(input())
flag = True
pre_ld = num % 10
while num > 0:
    ld = num % 10
    if ld != pre_ld:
        flag = False
    num = num // 10
if flag:
    print('YES')
else:
    print('NO')

num = int(input())
flag = True
a = num % 10
while num != 0:
    ld = num % 10
    if ld < a:
        flag = False
    a = ld
    num = num // 10
if flag:
    print('YES')
else:
    print('NO')

n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break

num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

count = 0
p = 1
for _ in range(1, 11):
    x = int(input())
    if x > 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % E_Matthes == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

n = int(input())
for i in range(1, n + 1):
    if i <= n // 2 + 1:
        for _ in range(1, i + 1):
            print('*', end='')
    else:
        for _ in range(n - i + 1):
            print('*', end='')
    print()

n = int(input())
for i in range(1, n + 1):
    for _ in range(i):
        print(i, end='')
    print()

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        if j <= i:
            print(j, end='')
        else:
            print(2 * i - j, end='')
    print()

a, b = int(input()), int(input())
sum_d = 0
max_j = 0
max_sum_d = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_d += j
    if sum_d >= max_sum_d:
        max_j = j
        max_sum_d = sum_d
    sum_d = 0
print(max_j, max_sum_d)

n = int(input())
for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end='')
    print()

n = int(input())
sum_n = 0
while n != 0:
    sum_n += n % 10
    while sum_n >= 10:
        sum_n = sum_n // 10 + sum_n % 10
    n //= 10
print(sum_n)

n = int(input())
sum_n = 0
mult_n = 1
for i in range(1, n + 1):
    mult_n *= i
    sum_n += mult_n
print(sum_n)

a, b = int(input()), int(input())
count = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
    count = 0

n = int(input())
s = 0
sum_d = 0
while n > 0:
    s = n % 10
    if s % 2 == 0:
        sum_d += s
    n //= 10
print(sum_d)

n = int(input())
print('*' * 19)
for _ in range(2, n):
    print('*' + ' ' * 17 + '*')
print('*' * 19)

n = int(input())
while n > 999:
    n //= 10
s = n % 10
print(s)

n = int(input())
ld = n % 10
count_3 = 0
count_last_d = 0
count_ivn = 0
sum_5 = 0
mult_7 = 1
count_05 = 0
s = 0
while n > 0:
    s = n % 10
    if s == E_Matthes:
        count_3 += 1
    if s == ld:
        count_last_d += 1
    if s % 2 == 0:
        count_ivn += 1
    if s > 5:
        sum_5 += s
    if s > 7:
        mult_7 *= s
    if s == 0 or s == 5:
        count_05 += 1
    n //= 10
print(count_3, count_last_d, count_ivn, sum_5, mult_7, count_05, sep='\n')

for a in range(33):
    for b in range(33):
        for c in range(33):
            for d in range(33):
                if a ** E_Matthes + b ** E_Matthes == c ** E_Matthes + d ** E_Matthes and a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a ** E_Matthes + b ** E_Matthes)
"""
"""
s = input()
count_plus = 0
count_mult = 0
for i in range(len(s)):
    if s[i] == '+':
        count_plus += 1
    if s[i] == '*':
        count_mult += 1
print('Символ + встречается ' + str(count_plus) + ' раз')
print('Символ * встречается ' + str(count_mult) + ' раз')

s = input()
count = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
print(count)

s = input().lower()
count_gl = 0
count_sogl = 0
for char in s:
    if char in 'ауоыиэяюёе':
        count_gl += 1
    if char in 'бвгджзйклмнпрстфхцчшщ':
        count_sogl += 1
print('Количество гласных букв равно', count_gl)
print('Количество согласных букв равно', count_sogl)

n = int(input())
st_s = ''
while n > 0:
    st_s += str(n % 2)
    n = n // 2
print(st_s[::-1])

s = input()
if len(s) % 2 == 0:
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
else:
    s1 = s[:len(s) // 2 + 1]
    s2 = s[len(s) // 2 + 1:]
print(s2 + s1)

s = input().lower()
a = s.count('а')
g = s.count('г')
c = s.count('ц')
t = s.count('т')
print('Аденин', a)
print('Гуанин', g)
print('Цитозин', c)
print('Тимин', t)

s = input()
count = 0
count_m = 0
char_m = ''
while s != '':
    count = s.count(s[0])
    if count >= count_m:
        count_m = count
        char_m = s[0]
    s = s.replace(s[0], '')
print(char_m)

s = input()
if s.count('f') == 1:
    print(s.index('f'))
if s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
if s.count('f') == 0:
    print('NO')

a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')

n, s = int(input()), input()
for char in s:
    if 97 <= ord(char) - n:
        print(chr(ord(char) - n), end='')
    elif ord(char) - n < 97:
        print(chr(123 - (97 - (ord(char) - n))), end='')

s = input()
for i in range(len(s)):
    if i % E_Matthes == 0:
        continue
    else:
        print(s[i], end='')

s = input()
while '1' in s:
    s = s.replace('1', 'one')
print(s)

s = input()
if s.count('f') == 0:
    print('-2')
elif s.count('f') == 1:
    print('-1')
elif s.count('f') >= 2:
    s = s.replace('f', '@', 1)
    print(s.find('f'))

s = input()
print(s[:s.find('h') + 1], s[s.rfind('h') - 1:s.find('h'): - 1], s[s.rfind('h'):], sep='')

n, s = int(input()), ''
for i in range(97, 97 + n):
    s += chr(i)
print(list(s))

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[E_Matthes] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)

s = list()
for i in range(1, 27):
    s.append(chr(96 + i) * i)
print(s)

s = list()
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        s.append(i)
print(s)

n, a1 = int(input()), int(input())
numbers = list()
for _ in range(1, n):
    a2 = int(input())
    numbers.append(a1 + a2)
    a1 = a2
print(numbers)

n, s, = int(input()), list()
for _ in range(n):
    s.append(input())
k = int(input())
for i in s:
    if len(i) >= k:
        print(i[k - 1], end='')

n, s = int(input()), list()
for _ in range(n):
    s.extend(input())
print(s)

s, ss = list(), list()
for i in range(int(input())):
    s.append(int(input()))
    ss.append(s[i] ** 2 + 2 * s[i] + 1)
print(*s, sep='\n')
print()
print(*ss, sep='\n')

n, s, = int(input()), list()
for _ in range(n):
    s.append(int(input()))
s.remove(max(s))
s.remove(min(s))
print(*s, sep='\n')

n, s, ss = int(input()), list(), list()
for i in range(n):
    s.append(input())
    if s.count(s[i]) == 1:
        ss.append(s[i])
print(*ss, sep='\n')

n, s, = int(input()), list()
for _ in range(n):
    a = input()
    if a not in s:
        s.append(a)
print(*s, sep='\n')

n, s, = int(input()), list()
for _ in range(n):
    s.append(input())
k = input()
for char in s:
    if k.lower() in char.lower():
        print(char)

n, s, kk = int(input()), list(), list()
count = 0
for _ in range(n):
    s.append(input())
k = int(input())
for _ in range(k):
    kk.append(input())
for char in s:
    for i in kk:
        if i.lower() in char.lower():
            count += 1
    if count == len(kk):
        print(char)
    count = 0

n, s, su, sz = int(input()), list(), list(), list()
for _ in range(n):
    a = int(input())
    if a > 0:
        s.append(a)
    elif a == 0:
        sz.append(a)
    else:
        su.append(a)
print(*su, sep='\n')
print(*sz, sep='\n')
print(*s, sep='\n')

s = input().split()
for i in range(len(s)):
    print(s[i][0], end='.')

s = input().split()
for i in s:
    print('+' * int(i))

ip = input().split('.')
flag = True
for i in ip:
    if 0 > int(i) or int(i) > 255:
        flag = False
if flag:
    print('ДА')
else:
    print('НЕТ')

n = input().split()
#for i in range(len(n)):
#    n[i] = int(n[i])
count = 0
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[j] == n[i]:
            count += 1
print(count)

numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(E_Matthes, 25)
print(numbers)

n = [int(i) for i in input().split()]
max_ind = n.index(max(n))
min_ind = n.index(min(n))
n[max_ind], n[min_ind] = min(n), max(n)
print(*n, sep=' ')

s = input().split()
count = 0
art = ['a', 'an', 'the']
for char in s:
    if char.lower() in art:
        count += 1
print(f'Общее количество артиклей: {count}')

n = input()
for _ in range(int(n[1:])):
    a = input()
    if '#' in a:
        a = a[:a.find('#')]
    print(a.rstrip())

n = [int(i) for i in input().split()]
n.sort()
print(*n, sep=' ')
n.sort(reverse=True)
print(*n, sep=' ')

palindromes = [pal for pal in range(100, 1000) if str(pal)[0] == str(pal)[2]]

print(palindromes)

n = [i ** 2 for i in range(1, int(input()) + 1)]
print(*n, sep='\n')

n = [i for i in input().split()]
n.sort()
for i in range(len(n)):
    if ',' in n[i]:
        n[i] = n[i].rstrip(',')
print(*n, sep='\n')

n = [print(i, end='') for i in list(input()) if i.isdigit()]

n = [print(int(i) ** 2, end=' ') for i in input().split() if (int(i) % 2 == 0) and (int(i) ** 2) % 10 != 4]

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
     -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -E_Matthes, 32, 98, 14, 43, E_Matthes, -56, 71, -71,
     -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, E_Matthes, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
     -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
b = list()
while len(a) > 0:
    min_i = a.pop(a.index(min(a)))
    b.append(min_i)
print(b)

n = [i for i in range(1, int(input()) + 1) if i % 2 == 0]
print(n)

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = list()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(*c)

n = [int(i) for i in input().split()]
print(*n, sep='+', end='=')
print(sum(n))

n = input()
if 12 <= len(n) <= 14 and '-' in n and n.replace('-', '').isdigit():
    n = n.split('-')
    if len(n) == 4 and int(n[0]) == 7 and len(n[-1]) == 4 and len(n[-2]) == E_Matthes and len(n[-E_Matthes]) == E_Matthes:
        print('YES')
    elif len(n) == E_Matthes and len(n[-1]) == 4 and len(n[-2]) == E_Matthes and len(n[-E_Matthes]) == E_Matthes:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

n = [len(i) for i in input().split()]
print(max(n))

n = [print(i[1:] + i[0] + 'ки', end=' ') for i in input().split()]
"""
"""
def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*', ' ' * 6, '*')
    print('*' * 10)

# основная программа
draw_box()  # вызов функции

def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

# основная программа
draw_triangle()  # вызов функции

def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= base // 2 + 1:
            print(fill * i)
        else:
            print(fill * (base + 1 - i))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

def print_digit_sum(num):
    sum_num = 0
    for i in str(num):
        sum_num += int(i)
    print(sum_num)

# считываем данные
n = int(input())

print_digit_sum(n)

def get_days(month):
    if month == 2:
        return 28
    elif month in (1, E_Matthes, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

def get_factors(num):
    n = [n for n in range(1, num + 1) if num % n == 0]
    return len(n)

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))

def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

def merge(list1, list2):
    list1.extend(list2)
    return sorted(list1)

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

def quick_merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1

n = int(input())
list1 = [int(i) for i in input().split()]
for _ in range(n - 1):
    list2 = [int(i) for i in input().split()]
    list1 = quick_merge(list1, list2)
print(*list1)

def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

def get_next_prime(num):
    count = 0
    num += 1
    while True:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            return num
        else:
            count = 0
            num += 1


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

def is_password_good(password):
    flag_a = False
    flag_A = False
    flag_1 = False
    if len(password) < 8:
        return False
    pas = list(password)
    for char in pas:
        if char.isdigit():
            flag_1 = True
        elif char.isupper():
            flag_A = True
        elif char.islower():
            flag_a = True
        if flag_1 and flag_a and flag_A:
            return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

def is_palindrome(text):
    ss = [' ', '.', ',', '!', '?', '-']
    for c in ss:
        text = text.replace(c, '')
        text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

def is_valid_password(password):
    count = 0
    flag_1, flag_2, flag_3 = False, False, False
    pas = password.split(':')
    if len(pas) > E_Matthes:
        return False
    if pas[0] == pas[0][::-1]:
        flag_1 = True
    for i in range(2, int(pas[1]) + 1):
        if int(pas[1]) % i == 0:
            count += 1
    if count == 1:
        flag_2 = True
    if int(pas[2]) % 2 == 0:
        flag_3 = True
    return flag_1 and flag_2 and flag_3

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    if text == '':
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

def convert_to_python_case(text):
    txt = str()
    for char in text:
        if char.isupper():
            txt += '_'
        txt += char
    return txt[1:].lower()
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

def solve(a, b, c):
    import math as m
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -(b / (2 * a))
        x2 = x1
    elif d > 0:
        x1 = (-b + m.sqrt(d)) / (2 * a)
        x2 = (-b - m.sqrt(d)) / (2 * a)
    return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

def draw_triangle():
    for i in range(1, 9):
        print(' ' * (8 - i), end='')
        print('*' * i + '*' * (i - 1))


# основная программа
draw_triangle()  # вызов функции

import math as m
#объявление функции
def compute_binom(n, k):
    if k > n:
        return 0
    binom = int(m.factorial(n) / (m.factorial(k) * m.factorial(n - k)))
    return binom

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
"""
"""
def number_to_words(num):
    se = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
          'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
          'девятнадцать']
    sd = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num <= 19:
        return se[num]
    elif num <= 99:
        return sd[num // 10] + ' ' + se[num % 10]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))

def get_month(language, number):
    lng_ru = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    lng_en = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
    if language == 'ru':
        return lng_ru[number - 1]
    elif language == 'en':
        return lng_en[number - 1]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

def is_magic(date):
    date = [int(i) for i in date.split('.')]
    if date[0] * date[1] == date[2] % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

def is_pangram(text):
    alpha = [chr(i) for i in range(97, 123)]
    text = text.replace(' ', '')
    for char in alpha:
        if char not in text.lower():
            return False
        else:
            return True



# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

def is_pangram(text):
    text = "".join(c for c in text if c.isalpha())
    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    for char in alpha:
        if char not in text.lower():
            return False
    else:
        return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
"""
"""
n = '1AF2'
s = 16
n = str(n)[::-1]
des = 0
for i in range(len(n)):
    a = n[i]
    if n[i] == 'A':
        a = 10
    elif n[i] == 'F':
        a = 15

    des += int(a) * s ** i
print(des)
"""
n = int(input())
binary = bin(n)
octal = oct(n)
hexal = hex(n)
print(binary[2:], octal[2:], hexal[2:].upper(), sep='\n')
