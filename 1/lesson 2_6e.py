n = int(input())
m = [[0 for j in range(n)] for i in range(n)]

l, r = 0, n - 1
u, d = 0, n - 1

ch = [int(i) for i in range(1, n ** 2 + 1)]

while len(ch) != 0:
    for i in range(l, r + 1):
        m[l][i] = ch.pop(0)
    u += 1
    for i in range(u, d + 1):
        m[i][r] = ch.pop(0)
    r -= 1
    for i in range(r, l - 1, -1):
        m[d][i] = ch.pop(0)
    d -= 1
    for i in range(d, u - 1, -1):
        m[i][l] = ch.pop(0)
    l += 1
for i in m:
    for j in i:
        print(j, end=' ')
    print()
