a=input().split()
c=a[0]
for i in a:
    if len(i)>len(c):
        c=i
print(c)
print(a.index(c))
