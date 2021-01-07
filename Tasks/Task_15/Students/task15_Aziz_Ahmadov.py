a=int(input())
b=str(a)[::-1]
s=''
q=3
for i in b:
    s+=i
    q-=1
    if q==0:
        s+=','
        q=3
if not len(b)%3:
    s=s[:-1]
print(s[::-1])
