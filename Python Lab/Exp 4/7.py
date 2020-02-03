celcius = int(input("Enter temperature in celcius: "))

farhenheit = lambda x: (x*(9/5))+32
print("The temperature in farhenheit is ", farhenheit(celcius))