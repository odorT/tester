n=input()
t=0
p=0
a=n.split(' ')
for i in a:
    if(t<len(i)):
        flag=p
        s=i;
        t=len(i)
    p+=1
print(s)
print(flag)
