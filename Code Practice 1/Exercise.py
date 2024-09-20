sales=int(input("Enter sales rupees: "))
if sales>=100000:
    basic=4000
    hra=20*basic/100
    da=110*basic/100
    conv=500
    inc=10*sales/100
    bonus=1000
else:
    basic=4000
    hra=10*basic/100
    da=110*basic/100
    conv=500
    inc=4*sales/100
    bonus=500
print("Basic= Rs",basic)
print("HRA= Rs",hra)
print("DA= Rs",da)
print("Conveyance= Rs",conv)
print("Incentive= Rs",inc)
print("Bonus= Rs",bonus)
print("------------------------")
print("Total= Rs",basic+hra+da+conv+inc+bonus)
print("------------------------")
