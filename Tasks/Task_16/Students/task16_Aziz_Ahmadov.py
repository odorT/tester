a=input()
s=[]
while a!='':
    s.append(a)
    a=input()
s=s[::-1]
for i in s:
    while s.count(i)>1:
        s.remove(i)
for i in s[::-1]:
    print(i)
