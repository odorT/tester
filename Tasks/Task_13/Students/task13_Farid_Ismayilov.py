n = int(input())
m = n
x = 0
while n>0:
    digit=n%10
    x = x*10+digit
    n = n//10
if m == x:
    print("palindrome")
else:
    print("not palindrome")
