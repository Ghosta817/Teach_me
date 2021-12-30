with open("C:\\1\\dataset_3363_2.txt") as inf:
    s = inf.readline().strip()

sch_d, ss = '', ''

for i in s[::-1]:
    if i.isdigit():
        sch_d += i
        continue
    else:
        ss += str(i) * int(sch_d[::-1])
        sch_d = ''

with open("C:\\1\\answer.txt", 'w') as ouf:
    ouf.write(ss[::-1])
