s=str(input())
l=s.split()
mx=len(l[0])
sx=l[0]
for i in range(len(l)):
    if len(l[i])>mx:
        mx=len(l[i])
        sx=l[i]
        id=i
print(sx)
print(id)
