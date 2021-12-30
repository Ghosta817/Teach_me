'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
'''

import requests

with open("C:\\1\\dataset_3378_3.txt", 'r') as inf:
    s = inf.read().strip()
a = requests.get(s)
while True:
    a = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + a.text)
    if 'We' in a.text:
        break
print(a.text)
