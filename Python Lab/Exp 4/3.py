
def digtobin(num, string):
    if num >= 1:
        if(num%2==0):
            string = string + '0'
            digtobin(num/2, string)
        else:
            string = string + '1'
            digtobin(int(num/2), string)
    else:
        print("The binary is ",string[len(string)::-1])

digit = int(input("Enter a number: "))
digtobin(digit, "")