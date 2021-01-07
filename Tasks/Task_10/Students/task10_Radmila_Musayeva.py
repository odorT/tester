a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print("equilateral")
elif a==b and b!=c:
    print("isosceles")
elif b==c and a!=c:
    print("isosceles")
elif a==c and a!=b:
    print("isosceles")
else:
    print("scalane")
