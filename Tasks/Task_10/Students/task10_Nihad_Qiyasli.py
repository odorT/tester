a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("equilateral")
elif a == b and not b == c and not a ==c:
    print("isosceles")
elif not a == b and not b == c and not a == c:
    print("scalene")
