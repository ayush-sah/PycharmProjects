

matrix1 = []
matrix2 = []
for a in range(2):
    print("Enter elements in Array ", a+1, ": ")
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(int(input()))
        if a == 0:
            matrix1.append(temp)
        else:
            matrix2.append(temp)

for i in range(3):
    for j in range(3):
        print(matrix1[i][j] + matrix2[i][j],end = " ")
    print()