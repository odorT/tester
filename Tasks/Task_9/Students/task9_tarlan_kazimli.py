b=int(input())
if b%400==0 :
    print("leap year")
elif b%100==0 :
    print("not leap year")
elif b%4==0 :
    print("leap year")
else :
    print("not leap year")