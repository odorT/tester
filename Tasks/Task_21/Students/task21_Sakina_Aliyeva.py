def UpOrLow (a):
    import string
    up=0
    low=0
    for i in a:
        if i in string.ascii_lowercase:
            low+=1
        elif i in string.ascii_uppercase:
            up+=1
    print(up)
    print(low)

UpOrLow(input())
