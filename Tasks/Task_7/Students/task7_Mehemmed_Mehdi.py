x = int(input())
a = x//1000
b = x//100 - a*10
c = (x%100 - x%10)//10
d = x%10

print(a*b*c*d)
