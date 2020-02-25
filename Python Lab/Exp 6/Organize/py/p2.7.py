t1=["January","March","May","July","August","October","December"]
t2=["April","June","September","November"]
Feb="28 or 29"
month=input("Enter the Month ")
while(1):
    
    if month=="February":
        print(Feb)
        break;
    elif month in t1:
        print("31")
        break;
    elif month in t2:
        print("30")
        break;
    else:
        break
