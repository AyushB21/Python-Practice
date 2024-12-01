li=[43,12,76,59,82,56,99]
li.sort() 
n=len(li)
f=0  #FIRST
k=0
l=n-1
ele=int(input("Enter element to search: "))
while f<=l:
    mi=(f+l)//2
    if li[mi]==ele:
        k=1
        break
    elif ele>li[mi]:
        f=mi+1
    elif ele<li[mi]:
        l=mi-1
if k==1:
    print("FOUND")
else:
    print("NOT FOUND")
