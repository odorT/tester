a=int(input())
c=0
for i in range(1,a):
    if a%i==0:
        c+=i
if c==a:
    print("True")
else:
    print("False")
        
