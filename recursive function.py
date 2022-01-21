# Python Core
def spell(txt):

    if len(txt) == 0:
        return txt
    else:
        return spell(txt[1:])+txt[0]


txt = input("Given a string: ")
spell(txt)

print(spell(txt))
