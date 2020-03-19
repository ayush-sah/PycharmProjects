import random 
guess=random.randint(1,10)
n=int(input("Guess the number"))

while(n!=guess):
    if(n<guess):
        print("Guess number greater than ",n)
        n=int(input("Guess the number"))
    elif(n>guess):
        print("Guess number smaller than ",n)
        n=int(input("Guess the number"))
print("Match found")
