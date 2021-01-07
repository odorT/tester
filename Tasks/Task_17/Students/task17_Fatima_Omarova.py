n=int(input())
import math
k=int(math.sqrt(n)+1)
sum=0
for i in range(1,k):
    if n%i==0:
        sum+=i
        if n/i!=i:
            sum+=n/i
sum=int(sum)-n
if sum==n:
    print("True")
else:
    print("False")
