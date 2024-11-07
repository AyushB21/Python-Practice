def alg():
    n=1
    while n==1:
        a=input("Enter you mail address: ")
        if a.find('@')== -1 or a.find('.')== -1:
            print("Invalid mail")
            continue
        else:
            print(a)
            break



