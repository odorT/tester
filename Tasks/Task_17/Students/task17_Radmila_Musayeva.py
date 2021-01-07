n=int(input())
sm=0
i=1
while i<n:
    if(n%i==0):
        sm+=i
    i+=1
if(sm==n):
    print("True")
else:
    print("False")
