class person:
    name = ""
    age = 0

    def __init__(self):
        self.name = input("Enter the name of the person: ")
        self.age = int(input("Enter the age of the person: "))

    def display(self):
        print("The name of the person is :", self.name, "and age is ", self.age)


class student:
    id = 0
    branch = ""

    def __init__(self):
        self.id = int(input("Enter ID no. of the student: "))
        self.branch = input("Enter the branch of the student: ")

    def display(self):
        print("The ID of the student is :", self.id, "and his branch is", self.branch)


class resident(person, student):
    def __init__(self):
        person.__init__(self)
        student.__init__(self)
        person.display(self)
        student.display(self)


p = resident()
