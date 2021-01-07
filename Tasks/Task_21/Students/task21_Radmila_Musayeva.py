s=input()
def calc(a):
    u=0
    l=0
    for i in a:
        if i==' ':
            continue
        if i.isupper():
            u+=1
        else:
            l+=1
    print(u)
    print(l)
calc(s)
