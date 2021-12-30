"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.
"""
n = int(input())
s = []
ss = {}
for i in range(n):
    s = input().strip().split(';')
    if s[0] not in ss:
        ss[s[0]] = [0] * 4
    if s[2] not in ss:
        ss[s[2]] = [0, 0, 0, 0]
    ss[s[0]][0] += 1
    ss[s[2]][0] += 1
    if int(s[1]) > int(s[3]):
        ss[s[0]][1] += 1
        ss[s[2]][3] += 1
    elif int(s[1]) < int(s[3]):
        ss[s[2]][1] += 1
        ss[s[0]][3] += 1
    elif int(s[1]) == int(s[3]):
        ss[s[0]][2] += 1
        ss[s[2]][2] += 1
for key, value in ss.items():
    value.append(value[1] * 3 + value[2])
    print(key + ':', *value)
