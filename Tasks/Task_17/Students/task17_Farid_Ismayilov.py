n = int(input())
sum1 = 0
for i in range(1,n): 
    if (n % i==0): 
        sum1 = sum1 + i
    else:
        sum1 = sum1 
if sum1 == n:
    print('True')
else:
    print('False')

