a=int(input())
b=int(input())
c=int(input())
if a==b & b==c:
  print ("equilateral")
elif a==b or b==c or a==c:
  print ("isoscales")
else:
  print("scalene")
