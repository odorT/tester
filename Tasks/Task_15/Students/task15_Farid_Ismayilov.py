n = input()
c = 0
b = len(n)
k = 1
d = 2
while int(n)>=1000 and b%3==0 and c!=b:
    if c+3==b:
        print(n[c:c+3],end=",")
    else:
        print(n[c:c+3],end=",")
    c=c+3
while int(n)>=1000 and b%3==1 and c!=b:
    print(n[0],end=",")
    b = b - 1
    while b%3==0 and c!=b:
        if c+3==b:
            print(n[k:k+3])
        else:
            print(n[k:k+3],end=",")
        k = k+3
        c = c + 3
while int(n)>=1000 and b%3==2 and c!=b:
    print(n[0:2], end=",")
    b = b - 2
    while b%3==0 and c!=b:
        if c+3==b:
            print(n[d:d+3])
        else:
            print(n[d:d+3],end=",")
        d=d+3
        c=c+3
if int(n)<1000 and n!=0:
    print(n)
