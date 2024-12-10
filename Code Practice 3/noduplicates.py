x=[13,52,59,14,32,7]
temp=[]
def Reverse(x):
    x.reverse()
    for i in x:
        ele=i*4
        temp.append(ele)
    print(temp)
