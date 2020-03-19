file = open("abc.txt", "r")

print("Text in file printed word by word.")
for line in file:
    for word in line.split():
        print(word)