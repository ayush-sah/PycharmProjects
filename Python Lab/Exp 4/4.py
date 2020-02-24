# To use lambda function on list to generate filtered list, mapped list and reduced list
import functools

l = [1,2,3,4,5,6,7,8,9,10]

addition = map(lambda x: x+x, l)
square = map(lambda x: x*x, l)
greaterthan9 = filter(lambda x:x>9,map(lambda x: x * x,l))
sumoflist = functools.reduce(lambda x,y:x+y,l)

print("After addition values are: ", list(addition))
print("After multiplication values are: ", list(square))
print("Numbers greater than 9 after square is ",list(greaterthan9))

print("The sum of the elements in the list is", sumoflist)
