# To merge two list and find second largest element in the list using bubble sort

l1 = []
l2 = []

num = int(input("Enter the number of elements you want to store int he first list: "))
print("Enter the elements of first list: ", end=" ")
while num > 0:
    l1.append(int(input()))
    num -= 1

num = int(input("Enter the number of elements you want to store int he second list: "))
print("Enter the elements of second list: ", end=" ")
while num > 0:
    l2.append(int(input()))
    num -= 1

l3 = l1 + l2
for i in range(len(l3)):
    j = i + 1
    for j in range(len(l3)):
        if l3[i] < l3[j]:
            temp = l3[i]
            l3[i] = l3[j]
            l3[j] = temp

print("The sorted array is ", l3, " with ", l3[len(l3) - 2], " being the second largest element.")
