def f(x):
    return x * 2 + 1

s, ss = [], {}
for i in range(int(input())):
    s.append(int(input()))
for key in s:
    if key not in ss.keys():
        ss[key] = f(key)
        print(ss[key])
    else:
        print(ss[key])
