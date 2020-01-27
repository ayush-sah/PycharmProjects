# Write a Python program to count the elements in a list until an element is a tuple

l1 = [1, 2, 3, 4, (5, 6, 7, 8), 9]
count = 0

for i in l1:
    if isinstance(i, tuple):
        break
    count += 1

print("The number of elements before tuple in the list is ", count)