n = int(input())
l = list()
s = 0
for i in range(1,n):
    if(n%i==0):
        l.append(i)
for i in l:
    s+=i
if(n==s): print(True)
else: print(False)
