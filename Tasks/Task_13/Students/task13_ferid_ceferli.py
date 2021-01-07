a=int(input())
b=a
rev=0
while a>0:
    n=a%10
    rev=rev*10+n
    a//=10
if rev==b:
    print("palindrome")
else:
    print("not palindrome")
