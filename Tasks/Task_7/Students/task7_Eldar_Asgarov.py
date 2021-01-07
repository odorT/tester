n=int(input())
product=1
while n>0:
    d=n%10
    product*=d
    n=n//10
print(product)

