print("Arithmetic Exception Handling: ")
try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("This statement is raising an arithmetic exception.")
else:
    print("Success.")
print()

print("Index Out of Bond Exception Handling: ")
try:
    a = [1, 2, 3]
    print(a[3])
except LookupError:
    print("Index out of bound error.")
else:
    print("Success")
print()

print("Import Error handling: ")
try:
    import NonExistantModule
except ModuleNotFoundError:
    print("Module you are trying to import not found.")
else:
    print("Success")
print()

print("Key Error Handling: ")
try:
    dict = {1: 10, 2: 20, 3: 30}
    print(dict[4])
except KeyError:
    print("Key not found in the dictionary.")
else:
    print("Success")
print()

print("Name Error Handling: ")
try:
    x = 10
    print(y)
except NameError:
    print("Invalid variable accessed.")
else:
    print("Success")
print()

print("Attribute Error Handling: ")
try:
    class c:
        pass
    ob = c()
    print(ob.data)
except AttributeError:
    print("Object does not support attribute references or attribute assignments.")
else:
    print("Success")
print()

print("Recursion Error Handling: ")
try:
    def recursion(x):
        recursion(x)
    print(recursion(0))
except RecursionError:
    print("Maximum Recursion depth is exceeded.")
else:
    print("Success")
print()

print("Overflow Error Handling: ")
try:
    import math
    print(math.exp(1000))
except OverflowError:
    print("Floating point operation failed.")
else:
    print("Sucess")
print()

print("Type Error Handling: ")
try:
    arr = ('tuple', ) + 'string'
    print(arr)
except TypeError:
    print("Objects of improper type.")
else:
    print("Success")
print()

print("Value Error Handling")
try:
    print(int('a'))
except ValueError:
    print("Invalid value.")
else:
    print("Success")
print()

