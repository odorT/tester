n = int(input())
a = 0
for i in range(1,n):
    if n % i == 0:
        a += i
if a == n:
    print(True)
else:
    print(False)
    
    
    
