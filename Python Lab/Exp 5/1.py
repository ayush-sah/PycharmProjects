# Python Program to Create a Class and Compute the Area and the Perimeter of the Circle

class circle:
    radius, a, peri = 0, 0, 0

    def __init__(self):
        self.radius = int(input("Enter the radius of cirle:"))

    def area(self):
        self.a = 3.14 * self.radius * self.radius

    def perimeter(self):
        self.peri = 2 * 3.14 * self.radius

    def display(self):
        print("The area of circle is:", self.a, "and its perimeter is ", self.peri)


c = circle()
c.area()
c.perimeter()
c.display()
