import re

number=input("")

pattern = "^[189][0-9]{7}$"
if re.match(pattern, number):
    print("Valid")
else:
    print("Invalid")
