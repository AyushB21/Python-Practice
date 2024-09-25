s1=eval(input("Enter 1st subject marks: "))
s2=eval(input("Enter 2nd subject marks: "))
s3=eval(input("Enter 3rd subject marks: "))
s4=eval(input("Enter 4th subject marks: "))
s5=eval(input("Enter 5th subject marks: "))
tot=s1+s2+s3+s4+s5
per=(tot/500)*100
print("Total marks: ",tot)
print("Percentage: ",round(per,2))
if per>=90:
    print("Distinction")
elif per>=80 and per<90:
    print("First Class")
elif per>=70 and per<80:
    print("Second Class")
elif per >=60 and per<70:
    print("Third Class")
elif per<60:
    print("Fail")
