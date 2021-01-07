n= int(input())

if n%400 ==0:
    print("leap year")
elif n%100 == 0:
    print("not leap year")
elif n% 4 == 0:
    print("leap year")
else:
    print("not leap year")
