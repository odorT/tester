#Task 13

num = int(input())
a = 0
a = num
eksi = 0

while num > 0:
    b = num % 10                 
    eksi = eksi * 10 + b 
    num //= 10  
    

if eksi == a:
  print("palindrome")
else:
  print("not palindrome")
