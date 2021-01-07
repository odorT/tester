n = int(input())
a = n//1000
b = n//100 - 10*a
c = n//10 - 100*a - 10*b
d = n - 1000*a - 100*b - 10*c
product = a*b*c*d
print(product)