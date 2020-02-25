import os


def readFile():
    file = open("abc.txt", "r")
    print(file.read())
    file.close()


def writeFile():
    file = open("abc.txt", "w")
    data = input("Enter what you want to write to the file: ")
    file.write(data)
    file.close()


def appendFile():
    file = open("abc.txt", "a")
    data = input("Enter what you want to write to the file: ")
    file.write(data)
    file.close()


def deleteFile():
    os.remove("abc.txt")
    print("File has been deleted.")


option = 0;
while True:

    option = int(input(
        "\n1. Read from file.\n2. Write to file.\n3. Append to file\n4. Delete the file.\n5. Exit\nEnter a action your want to perform: "))
    if option == 1:
        readFile()
    elif option == 2:
        writeFile()
    elif option == 3:
        appendFile()
    elif option == 4:
        deleteFile()
    elif option == 5:
        break
    else:
        print("Invalid input.")
