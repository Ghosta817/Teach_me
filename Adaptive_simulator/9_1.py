"""
A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A). For
scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.
"""

first, second = input().split()
trumps = input()

values = {'6': 1, '7': 2, '8': 3, '9': 4, '10': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}

if first[-1] == second[-1]:
    if values[first[:-1]] > values[second[:-1]]:
        print('First')
    else:
        print('Second')
elif trumps in first or trumps in second:
    if trumps in first:
        print('First')
    else:
        print('Second')
else:
    print('Error')



