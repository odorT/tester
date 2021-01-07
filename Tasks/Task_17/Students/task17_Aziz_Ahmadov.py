n=int(input())
s=[]
for i in range(1,n):
    if not n%i:
        s.append(i)
sum=0
for i in s:
    sum+=i
if sum==n:
    print("True")
else:
    print("False")
'''
for k in range(1,10000):
    s=[]
    for i in range(1,k):
        if not k%i:
            s.append(i)
    sum=0
    for i in s:
        sum+=i
    if sum==k:
        print("True",k)
'''
