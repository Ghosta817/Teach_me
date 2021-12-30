def encript(word):
    low_a = 'abcdefghijklmnopqrstuvwxyz'
    up_a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count_alpha = 0
    word_out = ''
    for char in word:
        if char.isalpha():
            count_alpha += 1
    for i in range(len(word)):
        if not word[i].isalpha():
            word_out += word[i]
        else:
            if word[i] == word[i].lower():
                for j in range(26):
                    if word[i] == low_a[j]:
                        word_out += low_a[(j + count_alpha) % 26]
                        break
            elif word[i] == word[i].upper():
                for j in range(26):
                    if word[i] == up_a[j]:
                        word_out += up_a[(j + count_alpha) % 26]
                        break
    return word_out


frz = input('Введите фразу на английском: \n').split()
frz_out = []
for word in frz:
    frz_out.append(encript(word))
print(' '.join(frz_out))
