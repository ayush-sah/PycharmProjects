# Convert the temperature in Celsius to Fahrenheit in list using anonymous  function

celsius = int(input("Enter temperature in celcius: "))

farhenheit = lambda x: (x*(9/5))+32
print("The temperature in farhenheit is ", farhenheit(celsius))