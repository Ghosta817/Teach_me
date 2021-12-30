"""
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a operator b
, где вместо operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения,
 вычитания, умножения и целочисленного деления.

input_string = input().split()
if input_string[1] == 'plus':
    print(int(input_string[0]) + int(input_string[2]))
elif input_string[1] == 'minus':
    print(int(input_string[0]) - int(input_string[2]))
elif input_string[1] == 'multiply':
    print(int(input_string[0]) * int(input_string[2]))
elif input_string[1] == 'divide':
    print(int(int(input_string[0]) / int(input_string[2])))
"""
import operator

input_string = input().split()
operators = {'plus': operator.add, 'minus': operator.sub, 'multiply': operator.mul, 'divide': operator.floordiv}
if input_string[2] == '0' and input_string[1] == 'divide':
    print(None)
else:
    print(operators[input_string[1]](int(input_string[0]), int(input_string[2])))

"""                         Красивое решение
def calc(a, op, b):
    c = {
        "plus": a + b,
        "minus": a - b,
        "multiply": a * b,
        "divide": a // b
    }
    return c[op]

s = input().split()
print(calc(int(s[0]), s[1], int(s[2])))
"""
