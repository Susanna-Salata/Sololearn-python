file = open("/usercode/files/books.txt", "r")

for line in file.readlines():
    word_list = line.split(" ")
    first_letter = ""
    for word in word_list:
        first_letter += word[0]
    print(first_letter)

file.close()
