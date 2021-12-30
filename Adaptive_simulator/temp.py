"""
def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

a_pipeline = find_odd_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)

s_list = ['a', '0', 'apple', 7, 'str', 285]
print(*s_list)
"""

n, m = [int(x) for x in input().split()]
input_field = [list(input()) for _ in range(int(n))]

print(input_field)
