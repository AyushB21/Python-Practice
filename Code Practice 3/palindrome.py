no=list(input("ENTER A DIGIT: "))
new="".join(no)
temp=no
temp.reverse()
final="".join(temp)
if new==final:
    print("YES")
else:
    print("NO")
