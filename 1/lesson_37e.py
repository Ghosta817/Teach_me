"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
"""

ss = {x: [0, 0] for x in range(1, 12)}
with open("C:\\1\\dataset_3380_5.txt", 'r') as inf:
    for i in inf:
        s = i.strip().split('\t')
        ss[int(s[0])][0] += int(s[2])
        ss[int(s[0])][1] += 1

for key in ss.keys():
    if ss[key][0] == 0:
        ss[key][0] = '-'
    else:
        ss[key][0] = ss[key][0] / ss[key][1]

with open("C:\\1\\answer3.txt", 'w') as ouf:
    for i in ss.keys():
        s = str(i) + ' ' + str(ss[i][0]) + '\n'
        ouf.writelines(s)
