# To shuffle a deck of cards and draw any 5 cards from it
import  random

def shuffle(num, type):
    print("Your random deck is: ")
    for i in range(5):
        newnum = random.choice(num)
        print("|",newnum, random.choice(type), end=" |\t")

numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
types = ["♠","♥","♦","♣"]
shuffle(numbers, types)

