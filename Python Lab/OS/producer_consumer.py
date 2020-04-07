s = 1
f = 0
e = int(input("Enter the size of buffer: "))

# mutex(s) will always be 1 after Producing ans consuming.

while True:
    action = int(input("\n1. Produce\n2. Consume\n3. Exit\nEnter action you want to perform: "))
    if action == 1:
        if s == 1 and e != 0:
            e -= 1
            f += 1
            print("Producer has produced.\nSemaphore E = ", e, "\nSemaphore F = ", f)
        else:
            print("Buffer is full.")
    elif action == 2:
        if s == 1 and f != 0:
            f -= 1
            e += 1
            print("Consumer has consumed.\nSemaphore E = ", e, "\nSemaphore F = ", f)
        else:
            print("Buffer is empty.")
    elif action == 3:
        break
    else:
        print("Invalid input. Try again.")
