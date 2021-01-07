def passwordchecker(x): #x=password
    n=0 #lower
    m=0 #upper
    b=0 #integer
    length=len(x)
    for i in x:
        if i==i.lower() and i==i.upper():
            b+=1
        elif i==i.lower():
            n+=1
        elif i==i.upper():
            m+=1
    if n==length or m==length or b==length:
        print("weak")
    elif n!=0 and m!=0 and b!=0:
        print("strong")
    else:
        print("moderate")
password=input()
passwordchecker(password)
