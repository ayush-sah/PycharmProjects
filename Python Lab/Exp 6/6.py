import random

rand = random.randrange(1, 100)
num = int(input("Enter a number: "))


class NotMatchingError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def NumberGame():
    try:
        num = int(input("Try Again: "))
        raise (NotMatchingError(num))

    except NotMatchingError as error:
        if(num>rand):
            print("Number too big", error.value)
            NumberGame()
        elif(num<rand):
            print("Number too small", error.value)
            NumberGame()
        print(error.value)

    else:
        print("Voila, same pinch.")
