a = int(input())
b = int(input())
c = int(input())

if a != b and b != c and a != c:
    print("scalene")
elif a == b and a == c and b ==c:
    print("equilateral")
else:
    print("isosceles")
