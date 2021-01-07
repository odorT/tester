a=int(input())
b=int(input())
c=int(input())

if a==b==c:
    print ("equilateral")
elif a==b or a==c or b==c:
    print ("isosceles")
else:
    print ("scalene ")
