import functools

l = [1,2,3,4,5,6,7,8,9,10]

print("The sum of the elements in the list is", functools.reduce(lambda x,y:x+y,l))