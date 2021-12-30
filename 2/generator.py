import random


def generator(lenght, sps, exc):
    alfa_sps = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!#$%&*+-=?@^_')
    bad_symb = 'il1Lo0O'
    password = ''
    for i in range(len(sps)):
        if sps[i] == 1:
            password += alfa_sps[i]
    if exc == 'y':
        for c in bad_symb:
            password.replace(c, '')
    password = list(password)
    random.shuffle(password)
    password = random.sample(password, lenght)
    return ''.join(password)


# superPas = input('Создать надежный пароль по преднастройкам или сами помучаетесь? (y/n) ')

cntPw = int(input('Укажите количество паролей для генерации: '))
lenPw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n) ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
sps = [0, 0, 0, 0]
if digOn == 'y':
    sps[0] = 1
if abcOn == 'y':
    sps[1] = 1
if ABCon == 'y':
    sps[2] = 1
if chOn == 'y':
    sps[3] = 1

for j in range(cntPw):
    pw = generator(lenPw, sps, excOn)
    print(pw)
