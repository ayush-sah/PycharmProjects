l = [1,2,3,4,5]
addition = map(lambda x: x+x, l)
square = map(lambda x: x*x, l)

print("After addition values are: ", list(addition))
print("After multiplication values are: ", list(square))