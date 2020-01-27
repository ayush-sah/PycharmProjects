# Input a number and display it is even or
repeat = True
while repeat:
    num = int(input("Enter a number: "))
    if num%2 == 0:
        print("It is Even Number.")
    else:
        print("It is Odd Number.")
    repeat = input("Do you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
