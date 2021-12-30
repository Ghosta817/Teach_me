"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if first_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
"""
import json

filename = 'C:\\1\\voyna-i-mir-tom.txt'

try:
    with open(filename) as read_obj:
        content = read_obj.read().rstrip()
except FileNotFoundError:
    err_message = 'Sorry, the file' + filename + 'not found.'
    print(err_message)
else:
    words = content.split()
    dif_words = dict()
    for word in words:
        for symbol in (',', '.', '!', '?', ';', ':', '...'):
            if symbol in word:
                word.replace(symbol, '')
        if word.lower() not in dif_words:
            dif_words[word.lower()] = 1
        else:
            dif_words[word.lower()] += 1
    max1 = ['', 0]
    max2 = ['', 0]
    max3 = ['', 0]
    for key, value in dif_words.items():
        if value >= max1[1]:
            max1 = [key, value]
        elif value >= max2[1]:
            max2 = [key, value]
        elif value >= max3[1]:
            max3 = [key, value]

filename = 'war_and_peace.json'
with open(filename, 'w') as f_object:
    json.dump(dif_words, f_object)


print(f'Всего в книге "Война и мир" примерно {len(words)} слов, из них уникальных: {len(dif_words)}.')
print(f'Три самых часто встреающихся слова: "{max1[0]}" встречается в тексте {max1[1]} раз, за ним следует'
      f' слово "{max2[0]}", оно встречается {max2[1]} раз и, наконец, "{max3[0]}" встречатеся {max3[1]} раз.\n')
print(f'Слово "Мир" встречатеся {dif_words["мир"]} раз, а "Война" {dif_words["война"]} раз! ')
