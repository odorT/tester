"""
The program takes a positive integer as an input and checks
whether it is palindrome or not.
"""
num = int(input())
temp = num
rev = 0
while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("palindrome")
else:
    print("not palindrome")
