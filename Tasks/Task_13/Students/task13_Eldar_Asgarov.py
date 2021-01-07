n=int(input())
num=n
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
if n==rev:
    print("palindrome")
else:
    print("not palindrome")
