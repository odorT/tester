a = int(input())
b = int(input())
c = int(input())
if(a!=0 and b!=0 and c!=0):
    if(a==b==c):
        print("equilateral")
    elif(a!=b and b!=c and a!=c):
        print("scalene")
    else:
        print("isosceles")
