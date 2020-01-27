repeat = True

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_name = ["jan", "feb", "march", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

while repeat:

    month = input("Enter Month: ")
    for i in range(12):
        if month == month_name[i]:
            print(month_days[i])

    repeat = input("Do you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
