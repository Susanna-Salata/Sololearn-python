# Python Data Structures
def balanced(expression):
    brackets = []

    for char in expression:
        if char == "(":
            brackets.insert(0, char)
        elif char == ")":
            if brackets:
                brackets.pop(0)
            else:
                return False

    if not brackets:
        return True
    else:
        return False


print(balanced(input()))
