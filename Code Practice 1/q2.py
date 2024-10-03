n="Animals Badger HoneyBee HoneyBadger"
c=0
for i in n:
    if i.isalpha():
        if i.isupper():
            x=ord(i)
            x=x+32
            print(chr(x),end='')
        elif i.islower():
            print(i,end='')
    elif i.isspace():
        print()
    else:
        print(i,end='')
    c=c+1
print()
