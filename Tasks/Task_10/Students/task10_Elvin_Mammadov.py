a=float(input())
b=float(input())
c=float(input())
if a==b==c:
    print("equilateral")
elif a==b!=c:
    print("isosceles")
elif a!=b==c:
    print("isosceles")
elif a==c!=b:
    print("isosceles")
else:
    print("scalene")
