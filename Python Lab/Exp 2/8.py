import random

rand = random.randrange(1,100)

num = int(input("Enter a number: "))

while num!=rand:
    if num > rand:
        print("Your number is too big.")
    else:
        print("Your number is too small.")
    num = int(input("Try Again: "))

print("Voila, same pinch.")