lines=[]
a=input()
while a:
    lines.append(a)
    a=input()
c=0
for i in lines:
    if lines.index(i)==c:
        print(i)
    c=c+1
