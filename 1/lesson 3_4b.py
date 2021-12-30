with open("C:\\1\\dataset_3363_3.txt", 'r') as inf:
    s = [i for i in inf.read().strip().lower().split()]

ss, r, k = {}, 0, []
for i in s:
    if i in ss:
        ss[i] += 1
    else:
        ss[i] = 1

for value in ss.values():
    if value > r:
        r = value

for key, value in ss.items():
    if value == r:
        k += key
k.sort()
print(k[0], r)


"""   Более простое решение без словарей, элегантно обыграна ситуация с лексиграфически первым словом.
with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))   """
