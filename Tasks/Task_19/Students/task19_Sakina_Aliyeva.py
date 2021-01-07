def password (a):
    import string
    checkLower=0
    checkHigher=0
    checkNum=0
    for i in a:
        if i not in string.ascii_letters:
            checkNum+=1
        elif i in string.ascii_lowercase:
            checkLower +=1
        elif i in string.ascii_uppercase:
            checkHigher +=1

    if checkNum>0 and checkLower>0 and checkHigher>0:
        print("strong")
    elif (checkNum>0 and checkLower>0) or (checkNum>0 and checkHigher>0) or (checkHigher>0 and checkLower>0):
        print("moderate")
    else:
        print ("weak")

password (input())

