year= int(input()) #1780
a=year%400
b=year%100
c=year%4

if a==0:
    print("leap year")

elif b==0 and a!=0:
    print ("not leap year")

elif c==0:
    print ("leap year")
    
else:
    print("not leap year")
