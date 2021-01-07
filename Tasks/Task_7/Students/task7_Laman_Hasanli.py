num = int(input())
d1 = num // 1000
d2 = num // 100 % 10
d3 = num // 10 % 10
d4 = num % 10
product = d1*d2*d3*d4
print(product)
