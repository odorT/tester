a=input()
b=len(a)
c=0
k=1
d=2
while int(a)>=1000 and b%3==0 and c!=b:
    if c+3==b:
        print(a[c:c+3])
    else:
        print(a[c:c+3],end=",")
    c=c+3
while int(a)>=1000 and b%3==1 and c!=b:
    print(a[0],end=',')
    b=b-1
    while b%3==0 and c!=b:
        if c+3==b:
            print(a[k:k+3])
        else:
            print(a[k:k+3],end=",")
        k=k+3
        c=c+3
while int(a)>=1000 and b%3==2 and c!=b:
    print(a[0:2],end=',')
    b=b-2
    while b%3==0 and c!=b:
        if c+3==b:
            print(a[d:d+3])
        else:
            print(a[d:d+3],end=",")
        d=d+3
        c=c+3
if int(a)<1000 and a!=0:
    print(a) 
    
