# Perform different operations on Tuple

t1 = (1, 2, 3, 4)
t2 = ('ayush', 'amish')

print("Concatenation of tuple: ", t1+t2)

t3 = (t1,t2)
print("\nNesting of tuple: ", t3)

t4 = ('ayush',)*3
print("\nRepetition of tuple: ", t4)

print("\nSlicing of tuples: ")
print(t1[1:])
print(t1[::-1])
print(t1[2:4])

print("\nLength of a tuple t3: ", len(t3))

l1 = [5,6,7,8]
print("\nConvert list into tuple: ", tuple(l1))

print("\nMax element in tuple t1: ", max(t1))
print("Min element in tuple t1: ", min(t1))