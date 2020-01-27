# WAP to validate a password

repeat = True
while repeat:

    password = input("Enter a password: ")
    special = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '\'', '\"', ':', ';', '<', '>', '/', '?', '{',
               '}',
               '[', ']']
    lower, upper, symbol, digit = 0, 0, 0, 0
    for a in password:
        if a.islower():
            lower += 1
        if a.isupper():
            upper += 1
        for s in special:
            if a == s:
                symbol += 1
        if a.isdigit():
            digit += 1

    if len(password) < 6:
        print("Password length must be greater than 6.")
    elif len(password) > 16:
        print("Password length must be lower than 16")
    elif lower == 0:
        print("Lower Case character missing.")
    elif upper == 0:
        print("Upper Case character missing.")
    elif symbol == 0:
        print("Special character missing.")
    elif digit == 0:
        print("Digit missing.")
    else:
        print("You entered a unique and valid password.")

    repeat = input("\nCheck another password ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
