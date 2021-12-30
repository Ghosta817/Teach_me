"""
Напишите программу, которая находит все позиции вхождения подстроки в строку.

Формат ввода:
На первой строке содержится исходная строка, на второй строке ввода указана подстрока, позиции которой требуется найти.
Строки состоят из символов латинского алфавита.

Формат вывода:
Строка, содержащая индексы (индексация начинается с нуля) вхождения подстроки в строку, разделённые пробелом или
число -1 в случае, когда подстрока не найдена.
"""
input_string = input()
substring = input()
out_index = str()

for i in range(len(input_string)):
    a = input_string[i:].find(substring)
    if not out_index and a == -1:
        print(-1)
        break
    elif a != -1 and str(a + i) not in out_index:
        out_index += str(a + i) + ' '
print(out_index)

"""                 Более простое решение
stroke, s = input(), input()
l = []
for i in range(len(stroke)-len(s)+1):
    if stroke[i:i+len(s)] == s:
        l.append(i)
if l:
    print(*l)
else:
    print('-1')
"""
