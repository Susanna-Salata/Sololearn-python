# Python Core
text = input()
dict = {}

for letter in text:
    if dict.get(letter):
        i = dict.get(letter) + 1
    else:
        i = 1

    dict.update({letter: i})

print(dict)


