T=(1,3,2,4,6,5)
new_tup=()
for i in range(len(T)):
    if i%2!=0:
        new_tup+=(T[i],)
print("New Tuple is: ",new_tup)
