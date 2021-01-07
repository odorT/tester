a=int(input())
if a%10==a//10000 and a//1000%10==a%100//10:
    print('palindrome')
else:
    print('not palindrome')
