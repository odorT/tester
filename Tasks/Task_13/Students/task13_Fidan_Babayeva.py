n = int(input())
m = n
a = 0
while n >0:
    digit = n % 10
    a = a * 10 + digit
    n = n // 10
if (m == a):
    print("palindrome")
else:
    print("not palindrome")
