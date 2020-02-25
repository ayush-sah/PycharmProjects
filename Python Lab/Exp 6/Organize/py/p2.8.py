pas=input("Enter your password")
l=len(pas)
ch=0
l1=0
n=0
length=0
if(l>=6 or l<=16):
    length+=1
    
for i in range(l):
    if(pas[i].isnumeric()):
        n+=1
    elif(pas[i].isalpha()):
        l1+=1
    elif(pas[i]=="$" or pas[i]=="#" or pas[i]=="@"):
        ch+=1


if(length==0 or n==0 or l1==0 or ch==0):
    print("Wrong Password")
else:
    print("Password accepted")
