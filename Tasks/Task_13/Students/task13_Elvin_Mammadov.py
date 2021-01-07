a=input()
b=0
c=0
for digit in a:
    c=c+int(digit)*10**b
    b=b+1
if int(a)==c:
    print("palindrome")
else:
    print("not palindrome")
