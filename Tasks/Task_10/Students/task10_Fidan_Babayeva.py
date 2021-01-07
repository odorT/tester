a = float(input())
b = float(input())
c = float(input())
if a == b == c:
    print("equilateral")
elif a == b:
    print("isosceles")
elif  a == c:
    print("isosceles")
elif b == c:
    print("isosceles")
else:
    print("scalene")

