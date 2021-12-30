coords = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}

for _ in range(int(input())):
    s = [i for i in input().lower().split()]
    coords[s[0]] += int(s[1])

print((coords['восток'] - coords['запад']), (coords['север'] - coords['юг']), sep=' ')
