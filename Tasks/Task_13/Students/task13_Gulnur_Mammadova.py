n = int(input())
a = 0
num = n
while(n != 0):
  b = n % 10
  a = a * 10 + b
  n = int(n / 10)
if(num == a):
  print("palindrome")
else:
  print("not palindrome")
