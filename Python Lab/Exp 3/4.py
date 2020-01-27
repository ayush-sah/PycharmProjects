# To add key value pair to the dictionary and search and then delete the given key from the dictionary
repeat = True
names = {'ayush': 'sah', 'dhiraj': 'rawat', 'sumit': 'sangwan'}

while repeat:
    action = int(input("1. Add\n2. Search\n3. Delete\n4. Exit\nEnter action no. you want to perform: "))
    if action == 1:
        key = input("Enter Key: ")
        value = input("Enter Key's value: ")
        names[key] = value
        print("Your Key and value has been inserted: ", names, "\n")

    elif action == 2:
        key = input("Enter key whose value you want to search: ")
        print("The value of ", key," is ", names[key], "\n")

    elif action == 3:
        key = input("Enter Key you want to delete: ")
        names.pop(key)
        print("Successfully Deleted. After deleting the dictionary is ", names, "\n")

    elif action == 4:
        print("Have a Good Day !!!")
        repeat = False

    else:
        print("Invalid Input. Try Again", "\n")



