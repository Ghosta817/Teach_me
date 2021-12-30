srd, mat, fiz, rus, stud = 0, 0, 0, 0, 0

with open("C:\\1\\dataset_3363_4.txt", 'r') as inf:
    ouf = open("C:\\1\\answer2.txt", 'w')
    for i in inf:
        s = i.strip().split(';')
        srd = ((int(s[1]) + int(s[2]) + int(s[3]))/3)
        ouf.write(str(srd) + '\n')
        mat += int(s[1])
        fiz += int(s[2])
        rus += int(s[3])
        stud += 1
    ss = [str(mat / stud), str(fiz / stud), str(rus / stud)]
    ouf.write(' '.join(ss))
    ouf.close()
