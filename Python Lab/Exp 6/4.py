import xlrd

file = xlrd.open_workbook("student.xlsx")
sheet = file.sheet_by_index(0)
print("Total Rows = ", sheet.nrows, "\nTotal Columns = ", sheet.ncols)
print()
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell_value(i, j), end="\t")
    print()

num = int(input("\nEnter Sr. no. whose data you want to display: "))
print()
print("Displaying data of student with Sr. : ", sheet.cell_value(num, 0))
print("Student name is: ", sheet.cell_value(num, 1))
print("Student marks in OS is: ", sheet.cell_value(num, 2))
print("Student marks in Python is: ", sheet.cell_value(num, 3))
