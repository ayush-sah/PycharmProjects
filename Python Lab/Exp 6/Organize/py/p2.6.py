r1=int(input("Enter rows of first matrix: "))
c1=int(input("Enter columns of first matrix: "))
r2=int(input("Enter rows of second matrix: "))
c2=int(input("Enter columns of second matrix: "))

if(r1==r2 and c1==c2):
    a = []
    b = []
    c = []
    print("Enter the elements of first matrix: ")

    for i in range(0,r1):
        a1 = []
        for j in range(0,c1):
            a1.append(int(input()))
        a.append(a1)

    print("Enter the elements of second matrix: ")
    
    for i in range(0,r2):
        b1=[]
        for j in range(0,c2):
            b1.append(int(input()))
        b.append(b1)

    print("First matrix")
    for i in range(0,r1):
        for j in range(0,c1):
            print(a[i][j], end=" ")
        print(end='\n')

    print("Second matrix")
    for i in range(0,r2):
        for j in range(0,c2):
            print(b[i][j], end=" ")
        print(end='\n')

    #Matrices addition
    for i in range(0,r2):
        c1=[]
        for j in range(0,c2):
            c1.append(a[i][j]+b[i][j])
        c.append(c1)

    print("Addition of matrices")

    for i in range(0,r2):
        for j in range(0,c2):
            print(c[i][j], end=" ")
        print(end='\n')

else:
    print("Matrices are not compatible for addition") 
