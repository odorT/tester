"""
Write a program that reads the lengths of 3 integer sides of a triangle. 
Display a message indicating the type of the triangle.
"""
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("equilateral")
elif a == b or a == c or b == c:
    print("isosceles")
else:
    print("scalene")
