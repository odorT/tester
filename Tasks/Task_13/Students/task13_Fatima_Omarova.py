n=int(input())
m=0
a=n
while(n>0):
    x=n%10
    m=10*m+x
    n//=10
print(m)
if(a==m):
    print("palindrome")
else:
    print("not palindrome")

    
