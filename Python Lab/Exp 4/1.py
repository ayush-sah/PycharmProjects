# To check whether string is palindrome or not using function recursion

repeat = True
while repeat:

    string = input("Enter a String: ")

    def palindrome(i, j, check=True):
        if i < j:

            if (string[i] != string[j]):
                return False

            else:
                i += 1
                j -= 1
                return palindrome(i, j)
        else:
            return True

    check = palindrome(0,len(string)-1)
    if check:
        print("Palindrome")
    else:
        print("Not a Palindrome")

    repeat = input("\nCheck another string ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
        continue
    else:
        repeat = False
