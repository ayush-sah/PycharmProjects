l = [1, 2, 3, 4, 5]
print("Numbers greater than 9 after square is ",list(filter(lambda x:x>9,map(lambda x: x * x,l))))
