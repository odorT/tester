a=int(input())
b=int(input())
c=int(input())
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
    
