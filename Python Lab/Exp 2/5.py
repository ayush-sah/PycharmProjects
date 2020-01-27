# To check whether the character entered is vowel or consonant

repeat = True
while repeat:

    ch = input("Enter an Alphabet: ")

    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    found = False

    for i in vowels:
        if i == ch:
            found = True

    if found:
        print("The alphabet you entered is a vowel.")
    else:
        print("The alphabet you entered is a consonant.")
    repeat = input("\nDo you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False

