"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
                    dict = {input().lower() for i in range(int(input()))}
"""
dict, ss = list(), set()
for _ in range(int(input())):
    dict.append(input().lower())

for _ in range(int(input())):
    for i in input().lower().split():
        ss.add(i)

print('\n'.join(ss.difference(dict)))

#print(*ss.difference(dict), sep="\n")
