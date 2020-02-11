# To Implement Operator Overloading in python


class calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return  self.value * other.value

    def __sub__(self, other):
        return self.value - other.value

    def __truediv__(self, other):
        return  self.value / other.value

    def __mod__(self, other):
        return self.value % other.value

    def __pow__(self, other):
        return self.value ** other.value

    def __lt__(self, other):
        if self.value < other.value:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if self.value == other.value:
            return "Both are equal"
        else:
            return "Both are not equal"


val1 = calculator(2)
val2 = calculator(3)
print("Addition of objects: ", val1 + val2)
print("Subtraction of objects: ", val1 - val2)
print("Multiplication of objects: ", val1 * val2)
print("Division of objects: ", val1 / val2)
print("Remainder of objects: ", val1 % val2)
print("Power of objects: ", val1 ** val2)
print("Comparison of objects: ", val1 < val2)
print("Checking equality of objects: ", val1 == val2)
