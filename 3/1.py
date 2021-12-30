"""
n = [int(input()) for _ in range(int(input()))]
print(sum(n))

x = [1, 2, E_Matthes]
print(id(x))
print(id([1, 2, E_Matthes]))
print(type(x))
print(type(4))
print(type(type(x)))

def s_s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s_s(b=31))

n, k = map(int, input().split())
def c(n, k):
    if k == 0 or n == k:
        return 1
    elif k > n:
        return 0
    else:
        return c(n - 1, k) + c(n - 1, k - 1)

print(c(n, k))



def create(ns, var):
    global namespaces
    namespaces[ns] = var
    add(ns, [])



def add(ns, var):
    global variables
    if ns not in variables.keys():
        variables[ns] = list(var)
    else:
        variables[ns].append(var)


def gett(ns, var):
    if var in variables[ns]:
        return ns
    else:
        while ns != None:
            for key, value in variables.items():
                if ns == key:
                    if var in value:
                        return key
                    else:
                        ns = namespaces[key]
    return None


namespaces = {'global': None}
variables = {'global': list()}

for _ in range(int(input())):
    cmd, ns, var = input().split()
    if cmd == 'create':
        create(ns, var)
    elif cmd == 'add':
        add(ns, var)
    else:
        print(gett(ns, var))
"""
"""

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.current_capacity = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity - self.current_capacity - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.current_capacity += v


a = MoneyBox(100)
print(a.can_add(98))
a.add(50)
print(a.can_add(51))
a.add(47)
print(a.can_add(4))
"""

with open('123.txt', encoding='utf-8') as fl:
    li = fl.read().split(', ')
    li.sort()

for i in li:
    print(i)
