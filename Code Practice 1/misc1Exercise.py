def countB(word):
    return word.count('b')

def count_Letter(word,letter):
    c=0
    for i in word:
        if i==letter:
            c=c+1
    return c

def modify_Case(word):
    return word.swapcase()

def getChar(word,pos):
    n=len(word)
    if pos>n:
        return("Out of Index")
    else:
        return word[pos-1]
