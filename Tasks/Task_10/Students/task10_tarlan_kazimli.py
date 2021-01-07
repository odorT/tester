a = int(input())
b = int(input())
c = int(input())

if a==b and a==c and c==b:
    print("equilateral")
elif a!=b and a==c and c!=b or a!=b and a!=c and c==b or a==b and a!=c and c!=b:
    print("isosceles")
elif a!=b and a!=c and c!=b:
    print("scalene")
