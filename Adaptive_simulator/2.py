"""
Напишите программу, которая выводит n первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно).
"""
"""
number = int(input())
count = 0
for i in range(1, number + 1):
    for _ in range(i):
        if count < number:
            print(i, end=' ')
            count += 1
"""
number = int(input())
num_list = str()
for i in range(1, number + 1):
    for _ in range(i):
        num_list += str(i)
print(" ".join(num_list[:number]))

"""             С помощью генератора списков
n=int(input())
print(*[x for x in range(1,(n+1)//2+1) for y in range(x)][:n])
"""
