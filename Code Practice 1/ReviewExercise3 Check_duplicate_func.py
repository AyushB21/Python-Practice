def check_duplicate(li):
    for i in li:
        if li.count(i)>1:
            return True
        else:
            return False
