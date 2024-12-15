def fun(str):          ##Without slicing
    rev=''
    for ch in str:
        rev=ch+rev
    print(rev)
def fun2(str):         #Using slicing
    rev=sttr[::-1]
