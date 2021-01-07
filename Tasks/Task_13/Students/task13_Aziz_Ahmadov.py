a=int(input())
a1=a
k=len(str(a))-1
vur=1
reverse=0
while a1>0:
    reverse+=a1%10*10**k
    a1//=10
    k-=1
if a==reverse:
    print('palindrome')
else:
    print('not palindrome')
