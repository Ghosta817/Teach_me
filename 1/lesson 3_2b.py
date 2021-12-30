s = [str(i) for i in input().lower().split()]
sss = {}
for i in set(s):
    sss[i] = s.count(i)
    print(i, sss[i])
