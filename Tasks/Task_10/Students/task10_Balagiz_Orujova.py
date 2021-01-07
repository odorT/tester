while True:
    a=int(input())
    b=int(input())
    c=int(input())
    if a==b and b==c and a==c:
        print("equilateral")
    elif a!=b and b!=c and c!=a:
        print("scalene")
    else:
        print("isosceles")
    


 
