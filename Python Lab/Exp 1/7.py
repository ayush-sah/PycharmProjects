# To compute compound interest given all the required values.

principal = int(input("Enter Principal: "))
roi = int(input("Enter Rate of Interest: "))
compounder = int(input("Enter No. of times interest compounded in a year: "))
time = int(input("Enter Time(in years): "))
roi = float(roi / 100)

amount = principal*((1 + (roi/compounder))**(compounder*time))

print("The total amount after applying compound interest will be ", amount)
