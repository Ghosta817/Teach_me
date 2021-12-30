def spin_words(sentence):
    s = [i for i in sentence.split()]
    for i in range(len(s)):
        if len(s[i]) >= 5:
            s[i] = s[i][::-1]
    return ' '.join(s)


# Второе более короткое решение
def spin_w(sent):
    return ' '.join(x[::-1] if len(x) >= 5 else x for x in sent.split())


# Проверка
s2 = spin_w('This is another test')
s = spin_words('This is another test')
print(s)
print(s2)

"""         Второе задание      """
def descending_order(num):
    return int(''.join(reversed([x for x in sorted(str(num))])))


# Второе более простое и наглядное решение
# Самое крутое: int(''.join(sorted(str(num), reverse=Truek)))
def descending_rdr(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)

# Проверка
n = descending_order(29390564870)
n2 = descending_rdr(29390564870)
print(n)
print(n2)
