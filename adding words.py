def concatenate(*args):
    text = args[0]
    for a in args[1:]:
        text += f"-{a}"

    return (text)


print(concatenate("I", "love", "Python", "!"))
