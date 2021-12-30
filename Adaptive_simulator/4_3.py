"""
Шифр Цезаря заключается в замене каждого символа входной строки на символ, находящийся на несколько позиций левее или
правее его в алфавите.

Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный
сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Используемый алфавит − - − пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу
вправо. На второй строке указывается непустая фраза для шифрования. Ведущие и завершающие пробелы не учитывать.
"""

c_dict = ' abcdefghijklmnopqrstuvwxyz'
num, input_string = int(input()), input().strip()

output_string = ''
num %= 27
for char in input_string:
    char_index = c_dict.find(char)
    if 0 <= char_index + num < len(c_dict):
        output_string += c_dict[char_index + num]
    elif char_index + num < 0:
        output_string += c_dict[len(c_dict) + (char_index + num)]
    elif char_index + num > len(c_dict) - 1:
        output_string += c_dict[(char_index + num) - len(c_dict)]

print(f'Result: "{output_string}"')
