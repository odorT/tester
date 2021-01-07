year = int(input())
a = year%400
b = year%4
c = year%100
if a==0:
    print("leap year")
elif c==0:
    print("not leap year")
elif b==0:
    print("leap year")
else:
    print("not leap year")
