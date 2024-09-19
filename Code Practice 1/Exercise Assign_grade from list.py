def Assign_grade(li):
    counter=1
    for i in li:
        if i>=90:
            grade="A"
        elif i>=80 and i<90:
            grade="B"
        elif i>65 and i<80:
            grade="C"
        elif i>=40 and i<=65:
            grade="D"
        elif i<40:
            grade="F"
        print("Student",counter," Marks",i, "grade", grade)
    
