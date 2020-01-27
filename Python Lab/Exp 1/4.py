# To find roots of quadratic equation

import math

print("Let the equation be Ax^2 + Bx + C\n")
A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))
C = int(input("Enter value of C: "))

D = (B*B)-(4*A*C)

if(D<0):
    print("Imaginary Roots")
elif(D==0):
    print(-B/2*A)
else:
    print(((-B)+math.sqrt(D))/2*A,((-B)-math.sqrt(D))/2*A)
    
