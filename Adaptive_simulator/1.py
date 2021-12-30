"""Перевод из арабских цифр в римские"""

rim_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
            4: 'IV', 1: 'I'}

arab_digit = int(input())
for i in (1000, 100, 10, 1):
    if arab_digit // i == 0:
        continue
    elif arab_digit // i < 4:
        print(rim_dict[i] * int(arab_digit // i), end='')
    elif 5 < arab_digit // i < 9:
        print(rim_dict[5 * i] + rim_dict[i] * (arab_digit // i - 5), end='')
    elif arab_digit // i * i in rim_dict:
        print(rim_dict[arab_digit // i * i], end='')
    arab_digit = arab_digit % i


"""                                 красивое и короткое решение

d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
n = int(input())
for i in d:
    if n // i != 0:
        print(d[i]*(n // i), end='')
        n %= i
        
"""
