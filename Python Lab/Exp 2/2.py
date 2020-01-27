# Display prime number between 1 and 100

import math

i = 1
print("Prime Numbers are: ")

while i <= 100:
    flag = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = False

    if i > 1:
        if flag:
            print(i, " ")

    i += 1
