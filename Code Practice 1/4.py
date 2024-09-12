def Count_Each_vowel(txt):
    d={}
    li=list(txt)
    for i in li:
        if i.lower() in ['a','e','i','o','u']:
            d[i]=li.count(i)
    return d
print(Count_Each_vowel("HELLO WORLD"))
