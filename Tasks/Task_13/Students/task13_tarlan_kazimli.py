#task 13
a=int(input())
t=a
b=0
while a>0:
    k=a%10
    b = b * 10 + k
    a = a // 10

if t==b :
    print("palindrome")
else:
   print("not palindrome")