n = input()

length = 0
for i in n:
    length += 1

n = int(n)

result = 0
q = int(length)
x = 0

while q > 0:
    a = n%10**q//10**(q-1)
    result += a * 10**x
    q -= 1
    x += 1

if result == n:
    print("palindrome")
else:
    print("not palindrome")