num=int(input())
check=""
keep=str(num)

while num!=0:
    rem=num%10
    num=num//10
    add=str(rem)
    check+=add

if check==keep:
    print("palindrome")
else:
    print("not palindrome")
