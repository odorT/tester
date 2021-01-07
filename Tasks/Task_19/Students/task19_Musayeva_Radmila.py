s=input()
def check(a):
    n=0
    u=0
    l=0
    for i in a:
        if i.isupper():
            u=1
        elif i.islower():
            l=1
        else:
            n=1
    sm=u+l+n
    if sm==3:
        print("strong")
    if sm==2:
        print("moderate")
    if sm==1:
        print("weak")
check(s)
