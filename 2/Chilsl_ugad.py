import random as r
my_num = r.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
print('Bведите целое число от 1 до 100: ')

def is_valid(number):
    if number.isdigit() and 0 < int(number) <= 100:
        return True
    else:
        return False


count = 0
while True:
    count += 1
    n = input()
    if not is_valid(n):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    n = int(n)
    if n > my_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    elif n < my_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали c {count} попыток, поздравляем!')
#        print('Сыграем еще ? (д/н или y/n)')
#        again = str(input())
#        if again == 'y' or again == 'д'
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
