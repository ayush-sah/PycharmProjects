# Create one dictionary of 5 students with their name, address, age, class and marks of 5 subjects. Perform all the
# operations on the created dictionary

students = {'roll': [1, 2, 3, 4, 5], 'name': ['Ayush', 'Sumit', 'Nikhil', 'Dhiraj', 'Sanket'],
            'address': ['Colaba', 'Andheri', 'Goregaon', 'Pune', 'Powai'], 'age': [23, 22, 21, 20, 19],
            'class': ['MCA', 'MBA', 'M.Tech', 'M.Sc', 'MA'],
            'marks': [[92, 95, 94, 98, 93], [92, 95, 94, 98, 93], [92, 95, 94, 98, 93], [92, 95, 94, 98, 93],
                      [92, 95, 94, 98, 93]]}
repeat = True
while repeat:
    subjects = ['English', 'Hindi', 'Marathi', 'Gujarati', 'Sanskrit']
    roll = int(input("Enter student's roll whose data you want to print: "))
    print("Name: ", students['name'][roll - 1])
    print("Address: ", students['address'][roll - 1])
    print("Age: ", students['age'][roll - 1])
    print("Class: ", students['class'][roll - 1])
    for i in range(5):
        print("Marks scored in", subjects[i], " : ", students['marks'][roll - 1][i])
    print("\nTotal Marks: ", sum(students['marks'][roll - 1]))
    print("\nPercentage: ", (sum(students['marks'][roll - 1]) / 500) * 100)

    repeat = input("\n\nDo you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
