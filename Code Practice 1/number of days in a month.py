m=int(input("Enter month number: "))
if m==2:
    y=int(input("Enter year: "))
    if (y%4==0 and y%100!=0):
        dy=29
    elif y%400==0:
        dy=29
    else:
        dy=28
elif m in [1,3,5,7,8,10,12]:
    dy=31
else:
    dy=30
print("Number of days=",dy)
            
