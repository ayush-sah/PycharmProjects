# To Implement a program with same method name and multiple arguments

class add:
    def calc(num1, num2):
        return num1 + num2


class concat(add):
    def calc(str1, str2):
        if type(str1) is int:
            return add.calc(str1, str2)
        else:
            return str1 + str2


print("The answer for int is:", concat.calc(12, 34))
print("The answer for string is:", concat.calc("Ayush", " Sah"))
