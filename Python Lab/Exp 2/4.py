# To check if the number is Armstrong or not
repeat = True
while repeat:
    num = int(input("Enter a number: "))
    power = 0
    temp = num
    while temp > 0:
        power += 1
        temp = int(temp / 10)

    sum = 0
    temp = num
    while temp > 0:
        sum += int((temp % 10) ** power)
        temp = int(temp / 10)

    if sum == num:
        print("Number entered is an Armstrong number.")
    else:
        print("Number entered is not an Armstrong number.")

    repeat = input("\nDo you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
