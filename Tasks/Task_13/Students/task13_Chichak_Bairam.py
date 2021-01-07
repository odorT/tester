# Task 13
num1 = int(input())
a = num1
b = 0

while num1 > 0:
  k = num1 % 10
  b = b * 10 + k
  num1 = num1 // 10

if a==b:
  print("palindrome")
else:
  print("not palindrome")