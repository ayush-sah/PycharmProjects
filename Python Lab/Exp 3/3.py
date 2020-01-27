# To count the occurrences of each word in a given string sentence

string = input("Enter a string: ")

words = string.split()
word = []
count = []
k = -1
for i in range(len(words)):
    j = i+1
    if words[i] in word:
        continue
    else:
        word.append(words[i])
        k = k + 1
        count.append(0)
    for j in range(len(words)):
        if words[i] == words[j]:
            count[k] += 1

for i in range(len(word)):
    print(word[i], ": ", count[i])