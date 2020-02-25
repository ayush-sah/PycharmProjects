import random

rand = random.randrange(1, 100)


def Numbergame(num):
    num
    try:
        if (num > rand):
            raise (BigNumber(num))
        elif (num < rand):
            raise (SmallNumber(num))

    except BigNumber as error1:
        print("Number too big,", error1.value)
        num = int(input("\nTry again: "))
        Numbergame(num)

    except SmallNumber as error2:
        print("Number too small,", error2.value)
        num = int(input("\nTry again: "))
        Numbergame(num)

    else:
        print("Voila, same pinch.")


class SmallNumber(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BigNumber(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


num = int(input("Enter a number: "))
Numbergame(num)
