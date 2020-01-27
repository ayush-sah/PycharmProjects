# Input marks of 5 subject and display result
repeat = True
while repeat:
    subjects = ["English", "Science", "Maths", "History", "Geography"]
    total = 0
    result = "Passed"

    for i in subjects:
        print("Enter marks for ", i, "(out of 100):")
        mark = int(input())
        if mark < 40:
            result = "Failed"
        total += mark

    print("\nThe student ", result, " total marks scored by student is ", total, " and the percentage scored by student is ", (total / 500) * 100)

    repeat = input("\nDo you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
