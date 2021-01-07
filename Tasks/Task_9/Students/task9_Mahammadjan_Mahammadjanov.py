n = int(input())
a = "leap year"
b = "not leap year"
if n%400 == 0:
    print(a)
elif n%100 == 0:
    print(b)
elif n%4 == 0:
    print(a)
else:
    print(b)