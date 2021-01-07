n = int(input())
a = n//1000
n%=1000
b = n//100
n%=100
c = n//10
n%=10
d = n
ans = a*b*c*d
print(ans)
