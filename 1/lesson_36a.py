""" Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests
 и посчитать число строк в нём. """

import requests

with open("C:\\1\\dataset_3378_2.txt", 'r') as inf:
    s = inf.read().strip()
a = [i for i in requests.get(s).text.splitlines()]
print(len(a))
