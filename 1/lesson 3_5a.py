""" Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля,
находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод. """

import math
pi = math.pi
r = float(input())
print(2 * pi * r)
