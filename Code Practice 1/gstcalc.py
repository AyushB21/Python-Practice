cgst=9/100
sgst=9/100
n=eval(input("Enter cost: "))
c=n*cgst
s=n*sgst
print()
print("\tINVOICE")
print()
print("Particulars","GST on Particulars",sep='\t')
print()
print("Cost ",n,sep='\t\t')
print("Add:CGST@9%",c,sep='\t')
print("Add:SGST@9%",s,sep='\t')
print("Total cost: ","Rs "+str(n+c+s),sep='\t')
