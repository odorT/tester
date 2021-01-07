#Number is abcd
#product is a*b*c*d
abcd = int(input())
a = abcd//1000
b = (abcd - 1000*a)//100
c = (abcd - 1000*a - 100*b)//10
d = abcd - 1000*a - 100*b - 10*c
print(a*b*c*d)
