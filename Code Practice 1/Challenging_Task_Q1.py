def maxConsecutive():
    m=int(input())
    n=int(input())
    if m<1 or m>10:
        print("m is greater than constraint")
    elif n<1 or n>31:
        print("n is greater than constraint")
    else:
        li=[]
        for i in range(n):
            data=input()
            if len(data)>m:
                return "Data greater"
            li.append(data)
        counter=[]
        for i in range(len(li)):
            c=0
            if (li[i]=="P"*m):  #Checking for all Present
                j=i
                while j<n:  #if all present,check consecutives
                    if li[j]=="P"*m:
                        c+=1
                        j+=1
                    else:
                        break   #If not cons. break
            counter.append(c)   #Add number of consec. for each

        print(max(counter)) #Find maximum consecutive
