a=int(input())
b=int(input())
c=int(input())
ortancil=a+b+c-max(a,b,c)-min(a,b,c)
if max(a,b,c)==min(a,b,c):
    print('equilateral')
elif max(a,b,c)==ortancil or min(a,b,c)==ortancil:
    print('isosceles')
else:
    print('scalene')
