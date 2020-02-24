# To Implement Multi-Level Inheritance in python
# Hierarchical Age Predictor

class Grandfather:
    age = 0

    def get_age(self, a):
        age = a + 20
        print("and your grandfather's age would be around", age)


class Father(Grandfather):
    age = 0

    def get_age(self, a):
        age = a + 20
        print("then your father age would be around", age, end=" ")
        super().get_age(age)


class Son(Father):
    age = 0
    name = ""

    def get_age(self, a):
        age = a
        print("If your age is", age, end=" ")
        super().get_age(age)


a = int(input("Enter your age: "))
Son().get_age(a)
