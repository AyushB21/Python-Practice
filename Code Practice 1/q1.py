n="Animals Badger HoneyBee HoneyBadger"
c=0
for i in n:
    if i.isalpha():
        if i.islower():
            x=ord(i)
            x=x-32
            print(chr(x),end='')
        elif i.isupper():
            print(i,end='')
    elif i.isspace():
        print()
    else:
        print(i,end='')
    c=c+1
print()

