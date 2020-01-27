# To calculate the no of uppercase ,lowercase letters and digits, spaces in a string

string = input("Enter a string: ")
lower, upper, digits, space = 0, 0, 0, 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        space += 1

print("There are ", lower, " lowercase letters, ", upper, " upper case letters, ", digits, " digits, ", space,
      " spaces.")
