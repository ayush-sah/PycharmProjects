# To concatenate two dictionaries and find sum of all values in dictionary
d1 = {}
d2 = {}
num = int(input("Enter the number of values you want to store int he first dictionary: "))
print("Enter value to store in the dictionary: ", end=" ")
for i in range(num):
    d1[i+1] = int(input())

num = int(input("Enter the number of values you want to store int he second dictionary: "))
print("Enter value to store in the dictionary: ", end=" ")
for j in range(num):
    d2[j+len(d1)+1] = int(input())

d1.update(d2)
print("After concatenation the dictionary is ", d1, " and sum of the values is ", sum(d1.values()))
