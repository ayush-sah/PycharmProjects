# To find Fibonacci series using recursion

def fibonacci(i, j, count):
    if count>0:
        print(i + j, end=" ")
        fibonacci(j, i+j, count-1)
    else:
        pass

count = int(input("Enter number of fibonacci digits you want to print Fibonacci series: "))
print("0 1", end = " ")
fibonacci(0,1,count-2)
